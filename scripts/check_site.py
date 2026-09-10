"""Browser regression checks. Requires an existing Playwright Python installation.
Run with the static site served at http://127.0.0.1:8765 (or --url).
No test dependency is shipped to visitors. Screenshots go to --output.
"""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('--url', default='http://127.0.0.1:8765')
parser.add_argument('--output', default='../../../_scratch/mom-v2-checks')
args = parser.parse_args()
output = Path(args.output)
output.mkdir(parents=True, exist_ok=True)
sizes = [(360, 800, 42), (390, 844, 42), (768, 1024, 39.96), (1440, 900, 58), (1900, 1080, 250)]
results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    for width, height, padding in sizes:
        page.set_viewport_size({'width': width, 'height': height})
        for route in ['/', '/watch/']:
            page.goto(args.url + route)
            page.screenshot(path=str(output / f'{width}-{"home" if route == "/" else "watch"}.png'), full_page=True)
            metrics = page.evaluate('''() => ({
                width: innerWidth, scrollWidth: document.documentElement.scrollWidth,
                padding: parseFloat(getComputedStyle(document.querySelector('.wrap')).paddingLeft),
                images: Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)
            })''')
            assert metrics['scrollWidth'] == width, metrics
            assert abs(metrics['padding'] - padding) < .1, metrics
            assert metrics['images'], metrics
            if route == '/':
                bottom = page.locator('.hero button').evaluate('(e) => e.getBoundingClientRect().bottom')
                assert bottom <= height, (width, bottom)
                page.locator('.hero button').click()
                assert page.locator('#hero-email').get_attribute('aria-invalid') == 'true'
                assert page.locator('#hero-email').evaluate('(e) => e === document.activeElement')
                page.locator('#hero-email').fill('test@example.com')
                page.locator('.hero button').click()
                assert 'has not been sent' in page.locator('#hero-status').inner_text()
                page.evaluate('window.scrollTo(0, 240)')
                page.wait_for_timeout(100)
                assert page.evaluate('''() => {
                    const hero = document.querySelector('.hero').getBoundingClientRect();
                    const visual = document.querySelector('.hero-visual').getBoundingClientRect();
                    return visual.top <= hero.top && visual.bottom >= hero.bottom;
                }''')
                transform = page.locator('.hero-visual').evaluate('(e) => getComputedStyle(e).transform')
                assert (transform == 'none') if width < 768 else (transform != 'none')
                page.emulate_media(reduced_motion='reduce')
                assert page.locator('.hero-visual').evaluate('(e) => getComputedStyle(e).transform') == 'none'
                page.emulate_media(reduced_motion='no-preference')
            else:
                assert page.locator('input').evaluate_all('(els) => els.map(e => e.name)') == ['first-name', 'last-name', 'email']
                page.locator('button').click()
                assert page.locator('#first-name').get_attribute('aria-invalid') == 'true'
                page.locator('#first-name').fill('Test')
                page.locator('#last-name').fill('Person')
                page.locator('#email').fill('test@example.com')
                page.locator('button').click()
                assert 'have not been sent' in page.locator('#watch-status').inner_text()
                assert page.locator('#reveal').is_hidden()
            results.append({'viewport': f'{width}x{height}', 'route': route, **metrics})
    # Provider responses are intercepted locally; no email leaves the browser.
    for response_body, code, state in [({'success': True}, 200, 'success'), ({'success': False}, 200, 'error'), ({'success': True}, 500, 'error')]:
        page.route('**/assets/js/signup-config.js', lambda route: route.fulfill(body="window.MOM_SIGNUP={endpoint:'/test-signup',emailField:'email',extraFields:{list:'mom'},isAccepted:(r,b)=>r.ok&&b.success===true,successMessage:'Request accepted.'};", content_type='text/javascript'))
        page.route('**/test-signup', lambda route: route.fulfill(status=code, json=response_body))
        page.goto(args.url)
        for selector in ['#hero-newsletter-form', '#newsletter-form']:
            form = page.locator(selector)
            form.locator('[type=email]').fill('test@example.com')
            form.locator('button').click()
            page.wait_for_function('(s) => document.querySelector(s + " .form-status").dataset.state !== "pending"', arg=selector)
            assert form.locator('.form-status').get_attribute('data-state') == state
            assert form.locator('button').is_enabled()
        page.unroute('**/assets/js/signup-config.js')
        page.unroute('**/test-signup')
    # Hold a request open to inspect loading/duplicate-submit behavior, then fail and retry.
    page.route('**/assets/js/signup-config.js', lambda route: route.fulfill(body="window.MOM_SIGNUP={endpoint:'/test-signup',isAccepted:(r,b)=>r.ok&&b.success===true,successMessage:'Request accepted.'};", content_type='text/javascript'))
    page.goto(args.url)
    page.evaluate('''() => {
        window.testRequests = 0;
        window.fetch = () => { window.testRequests++; return new Promise((resolve, reject) => { window.finishRequest = resolve; window.failRequest = reject; }); };
    }''')
    page.locator('#hero-email').fill('test@example.com')
    page.locator('.hero button').click()
    assert page.locator('.hero button').is_disabled()
    assert page.locator('#hero-newsletter-form').get_attribute('aria-busy') == 'true'
    page.locator('#hero-newsletter-form').evaluate('(form) => form.dispatchEvent(new Event("submit", {cancelable: true}))')
    assert page.evaluate('window.testRequests') == 1
    page.evaluate('window.failRequest(new TypeError("Network failed"))')
    page.wait_for_function('document.querySelector("#hero-status").dataset.state === "error"')
    assert page.locator('#hero-email').input_value() == 'test@example.com'
    page.locator('.hero button').click()
    page.evaluate('window.finishRequest(new Response(JSON.stringify({success:true}), {status:200}))')
    page.wait_for_function('document.querySelector("#hero-status").dataset.state === "success"')
    assert page.locator('#hero-email').input_value() == ''
    page.unroute('**/assets/js/signup-config.js')
    nojs = browser.new_context(java_script_enabled=False, viewport={'width': 360, 'height': 800})
    fallback = nojs.new_page()
    fallback.goto(args.url)
    assert fallback.locator('.hero button').is_disabled()
    assert 'unavailable' in fallback.locator('#hero-status').inner_text()
    assert fallback.locator('.hero-visual').is_visible()
    assert not errors, errors
    browser.close()
print(json.dumps(results, indent=2))
print('PASS: viewport, padding, assets, forms, provider response, reduced motion, no-JS checks')
