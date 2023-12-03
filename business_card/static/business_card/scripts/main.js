// Add class on scroll
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

// Toggle sidebar visibility
$(document).ready(function() {
  $('#nav-burger').on('click', function() {
    $('#sidebar').toggleClass('visible');
  });
});

// Smooth scroll to section
$(document).ready(function(){
	$("nav").on("click","a", function (event) {
		event.preventDefault();
		let id  = $(this).attr('href'),
            top = $(id).offset().top - 90;
		$('body,html').animate({scrollTop: top}, 1000);
        $('#sidebar').removeClass('visible');
	});
});

// Highlight active section in the navigation
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

// Disable dragging for images and links
$("img, a").on("dragstart", function(event) { event.preventDefault(); });

function showModal(id) {
    document.getElementById(id).showModal()
    console.log('show modal: ', id)
}
