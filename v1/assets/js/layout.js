/* MOM site — fluid side-padding via JS interpolation.
   forward.movie's own responsive padding is computed by Squarespace's
   fluid-layout engine, which is JavaScript-driven (not a static CSS
   formula) — confirmed 2026-09-01 by measuring the same element's padding
   at 9 viewport widths and finding the growth curve is non-linear
   (nearly flat below ~1300px, then increasingly steep). No single CSS
   clamp() reproduces that shape, so this does the same thing they do:
   compute it in JS on load/resize, from real measured breakpoints.

   Table below: [viewportWidth, sidePaddingPx], measured directly against
   forward.movie's live DOM (Synopsis heading's left offset) at each width.
   Values between breakpoints are linearly interpolated; below/above the
   table's ends, the nearest known value holds. */

(function () {
  var BREAKPOINTS = [
    [700, 42],
    [900, 36],
    [1000, 40],
    [1150, 46],
    [1300, 52],
    [1440, 58],
    [1650, 118],
    [1750, 168],
    [1900, 250],
  ];

  function paddingForWidth(w) {
    if (w <= BREAKPOINTS[0][0]) return BREAKPOINTS[0][1];
    var last = BREAKPOINTS[BREAKPOINTS.length - 1];
    if (w >= last[0]) return last[1];
    for (var i = 0; i < BREAKPOINTS.length - 1; i++) {
      var a = BREAKPOINTS[i], b = BREAKPOINTS[i + 1];
      if (w >= a[0] && w <= b[0]) {
        var t = (w - a[0]) / (b[0] - a[0]);
        return a[1] + t * (b[1] - a[1]);
      }
    }
    return last[1];
  }

  function apply() {
    var px = paddingForWidth(window.innerWidth);
    document.documentElement.style.setProperty('--page-x-live', px + 'px');
  }

  apply();
  window.addEventListener('resize', apply);
})();
