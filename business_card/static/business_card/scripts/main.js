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


$(document).ready(function() {
  $('#nav-burger').on('click', function() {
    $('#sidebar').toggleClass('visible');
  });
});

// $(document).ready(function() {
//     $(window).on('click', function(event) {
//         if (event.target != $('#sidebar')) {
//             $('nav-sidebar__link').toggleClass('visible');
//         }
//   });
// });
// // const container = document.getElementById("container")
// const sidebar = document.getElementById("sidebar")
// const openSidebar = () => {
//     // sidebar.classList.toggle("sidebar--is-hidden")
//     if (sidebar.style.display === "block") {
//         sidebar.style.display = "none"
//     } else {
//         sidebar.style.display = "block"
//     }
// }

$(document).ready(function(){
	$("nav").on("click","a", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();

		//забираем идентификатор блока с атрибута href
		let id  = $(this).attr('href'),

		//узнаем высоту от начала страницы до блока на который ссылается якорь
            top = $(id).offset().top - 90;

		//анимируем переход на расстояние - top за 1000 мс
		$('body,html').animate({scrollTop: top}, 1000);

        $('#sidebar').removeClass('visible');
	});
});

$(window).scroll(function(){
    let $sections = $('section');
    $sections.each(function(i,el){
        let top = $(el).offset().top - 100;
        let bottom = top + $(el).height();
        let scroll = $(window).scrollTop();
        let id = $(el).attr('id');
    	if (scroll >= top && scroll <= bottom) {
            $('a.active').removeClass('active');
            $('a[href="#'+id+'"]').addClass('active');
        }
    })
 });

$("img, a").on("dragstart", function(event) { event.preventDefault(); });

function openDialog(nameDialog) {
    let dialog = document.querySelector(nameDialog);
    dialog.show(); // Показываем диалоговое окно
}

