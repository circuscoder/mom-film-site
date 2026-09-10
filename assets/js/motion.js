/* The opening production still drifts behind stable text/forms. Measurements
   happen on resize only; scroll work is one passive, batched transform. */
(function () {
  'use strict';
  var hero = document.querySelector('.hero');
  var visual = document.querySelector('.hero-visual');
  if (!hero || !visual) return;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  var desktop = matchMedia('(min-width: 768px)');
  var frame = 0;
  var height = 1;
  var top = 0;
  var enabled = false;
  function render() {
    frame = 0;
    var progress = Math.max(0, Math.min(1, (window.scrollY - top) / height));
    visual.style.transform = enabled ? 'translate3d(0,' + (progress * 28).toFixed(2) + 'px,0)' : '';
  }
  function schedule() { if (!frame && enabled) frame = requestAnimationFrame(render); }
  function refresh() {
    enabled = !reduced.matches && desktop.matches;
    height = hero.offsetHeight;
    top = hero.offsetTop;
    visual.style.willChange = enabled ? 'transform' : '';
    render();
  }
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', refresh, { passive: true });
  reduced.addEventListener('change', refresh);
  desktop.addEventListener('change', refresh);
  refresh();
})();
