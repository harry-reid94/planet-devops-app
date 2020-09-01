window.onload = function() {
    new Glider(document.querySelector('.slider-list'), {
    // `auto` allows automatic responsive
    // width calculations
    slidesToShow: 1,

    // Force centering slide after resize event
    resizeLock: true,

    // arrow container elements or selector
    arrows: {
      prev: document.querySelector('[data-slider-prev]'),
      next: document.querySelector('[data-slider-next]')
    },

    responsive: [
      {
        breakpoint: 880,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        }
      }
    ]
  });

  document.addEventListener('glider-loaded', hideFFScrollBars);
  document.addEventListener('glider-refresh', hideFFScrollBars);

  function hideFFScrollBars(e) {
    var scrollbarHeight = 17; // Currently 17, may change with updates
    if (/firefox/i.test(navigator.userAgent)) {
      // We only need to appy to desktop. Firefox for mobile uses
      // a different rendering engine (WebKit)
      if (window.innerWidth > 575) {
        e.target.parentNode.style.height = (e.target.offsetHeight - scrollbarHeight) + 'px'
      }
    }
  }
};