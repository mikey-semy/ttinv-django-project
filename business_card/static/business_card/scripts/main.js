console.log('start')
$(document).ready(function() {
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 200) {
      $("#header").addClass("header--scrolled");
      $("#logo-main-img").addClass("logo-main__img--scrolled");
      $("#logo-main-text").addClass("logo-main__text--scrolled");

    } else {
      $("#header").removeClass("header--scrolled");
      $("#logo-main-img").removeClass("logo-main__img--scrolled");
      $("#logo-main-text").removeClass("logo-main__text--scrolled");
    }
  });
});