$(document).ready(function() {
  $(window).scroll(function() {
    let scroll = $(window).scrollTop();
    if (scroll >= 100) {
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

// const container = document.getElementById("container")
const sidebar = document.getElementById("sidebar")
const openSidebar = () => {
    // sidebar.classList.toggle("sidebar--is-hidden")
    if (sidebar.style.display === "block") {
        sidebar.style.display = "none"
    } else {
        sidebar.style.display = "block"
    }
}

$(document).ready(function(){
	$("#nav-main").on("click","a", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();

		//забираем идентификатор бока с атрибута href
		let id  = $(this).attr('href'),

		//узнаем высоту от начала страницы до блока на который ссылается якорь
			top = $(id).offset().top - 100;

		//анимируем переход на расстояние - top за 1500 мс
		$('body,html').animate({scrollTop: top}, 1000);
	});
});