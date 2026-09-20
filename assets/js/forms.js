(function () {
  'use strict';
  var config = window.MOM_SIGNUP;
  document.querySelectorAll('[data-newsletter], #watch-form').forEach(function (form) {
    var button = form.querySelector('button[type="submit"]');
    var status = form.querySelector('.form-status');
    var originalLabel = button.textContent;
    var isWatch = form.id === 'watch-form';
    var fields = Array.from(form.querySelectorAll('input[required]'));
    var pending = false;
    button.disabled = false;
    if (!isWatch && config && config.endpoint) status.textContent = '';
    fields.forEach(function (field) {
      field.addEventListener('input', function () {
        field.removeAttribute('aria-invalid');
        if (!pending && status.dataset.state === 'invalid') status.textContent = '';
      });
    });
    form.addEventListener('submit', async function (event) {
      event.preventDefault();
      if (pending) return;
      var invalid = fields.find(function (field) { return !field.validity.valid; });
      fields.forEach(function (field) { field.removeAttribute('aria-invalid'); });
      if (invalid) {
        status.dataset.state = 'invalid';
        status.textContent = invalid.type === 'email' ? 'Enter a valid email address, such as you@example.com.' : 'Enter your ' + (invalid.name === 'first-name' ? 'first' : 'last') + ' name.';
        invalid.setAttribute('aria-invalid', 'true');
        invalid.focus();
        return;
      }
      status.dataset.state = 'error';
      if (isWatch) {
        status.textContent = 'Trailer access is not available yet. Your details have not been sent. Please check back soon.';
        return;
      }
      if (!config || !config.endpoint) {
        status.textContent = 'Signup is not available yet. Your email has not been sent. Please check back soon.';
        return;
      }
      pending = true;
      button.disabled = true;
      button.textContent = 'Joining…';
      form.setAttribute('aria-busy', 'true');
      status.dataset.state = 'pending';
      status.textContent = 'Sending your signup request…';
      var controller = new AbortController();
      var timeout = setTimeout(function () { controller.abort(); }, 15000);
      try {
        var endpoint = new URL(config.endpoint, location.href);
        if (endpoint.protocol !== 'https:' && endpoint.origin !== location.origin) throw new Error('Invalid endpoint');
        var data = new FormData();
        Object.entries(config.extraFields || {}).forEach(function (entry) { data.append(entry[0], entry[1]); });
        data.set(config.emailField || 'email', form.querySelector('[type="email"]').value.trim());
        var response = await fetch(endpoint.href, {
          method: 'POST', body: data, headers: { Accept: 'application/json' },
          credentials: 'omit', signal: controller.signal
        });
        var body = await response.json();
        if (!config.isAccepted(response, body)) throw new Error('Subscription not confirmed');
        status.dataset.state = 'success';
        status.textContent = config.successMessage;
        form.reset();
      } catch (error) {
        status.dataset.state = 'error';
        status.textContent = 'We couldn’t confirm your signup. Please try again. If you received a confirmation email, follow its instructions.';
      } finally {
        clearTimeout(timeout);
        pending = false;
        button.disabled = false;
        button.textContent = originalLabel;
        form.removeAttribute('aria-busy');
      }
    });
  });
})();
