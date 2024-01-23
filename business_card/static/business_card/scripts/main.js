// Add class on scroll
$(document).ready(function() {
  $(window).scroll(function() {
    
    let scroll = $(window).scrollTop();
    console.log(scroll)
      if (scroll >= 1) {
        $('#header').addClass('fixed-top');
        if (scroll >= 100) {
          $("#header").addClass("header--scrolled");
          $("#logo-main-img").addClass("logo-main__img--scrolled");
          $("#logo-main-text").addClass("logo-main__text--scrolled");

        } else {
          $("#header").removeClass("header--scrolled");
          $("#logo-main-img").removeClass("logo-main__img--scrolled");
          $("#logo-main-text").removeClass("logo-main__text--scrolled");
        }
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
    let href = $(this).attr('href');
    if (!href.startsWith('#')) {
      return;
    }
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

$(document).on('ready', function () {
    // initialization of slick carousel
    $('.js-slide').slick({
        infinite: true,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
    });
  });

  function getScrollbarWidth() {

    // Creating invisible container
    const outer = document.createElement('div');
    outer.style.visibility = 'hidden';
    outer.style.overflow = 'scroll'; // forcing scrollbar to appear
    outer.style.msOverflowStyle = 'scrollbar'; // needed for WinJS apps
    document.body.appendChild(outer);
  
    // Creating inner element and placing it in the container
    const inner = document.createElement('div');
    outer.appendChild(inner);
  
    // Calculating difference between container's full width and the child width
    const scrollbarWidth = (outer.offsetWidth - inner.offsetWidth);
  
    // Removing temporary elements from the DOM
    outer.parentNode.removeChild(outer);
  
    return scrollbarWidth;
  
  }

  function applyPaddingForScrollbar() {
    let bodyScrollable = document.body.scrollHeight >= window.innerHeight
    if (bodyScrollable) {
      document.body.style.paddingRight = '0px'
    } else {
      document.body.style.paddingRight = `${getScrollbarWidth}px`
    }
  }

  const resizeObserver = new ResizeObserver((entries) => {
    applyPaddingForScrollbar()
  })
  resizeObserver.observe(document.body)