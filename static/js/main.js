jQuery(function ($) {
	

    // Calcular Alto de Navbar Fixed-Top
	$(function(){
        var Alto_Navbar_FixedTop = $('.container-NavBar').css('height');
        var Ancho_Sidebar = $('.sidebar-wrapper').css('width');
        var Ancho_btn_Autenticarse = $('.btn-autenticarse').css('width');
        var Alto_Sidebar_Footer = $('.sidebar-footer').css('height');
        
        $('.footer-general').css('height', parseInt(Alto_Sidebar_Footer));
        // Especificar Height del footer-general con el alto de sidebar-footer
        
        //$('.footer-general').css('left', parseInt(Ancho_Sidebar));
        // Mover a la derecha el footer-general  
        $('.btn-registrarse').css('width', parseInt(Ancho_btn_Autenticarse) + "px");
          // Igualar Anchos de Botones Registrarse y Autenticarse
        $('.ancho-cabezal-navbar').css('width', parseInt(Ancho_Sidebar));
          // Dar width con el sidebar a navbar-header
        $('.barra').css('top', parseInt(Alto_Navbar_FixedTop));
          // Dar Top al Page-Content
        $('.page-content').css('top', parseInt(Alto_Navbar_FixedTop) - 40 + "px");
          // $('.sidebar-wrapper').css( { 'height': 'calc(100% - ' + 100 + 'px)', 'max-height': 'calc(100% - ' + 100 + 'px)'  });
        $('.sidebar-wrapper').css( { 'height': 'calc(100% - ' + parseInt(Alto_Navbar_FixedTop) + 'px)', 'max-height': 'calc(100% - ' + parseInt(Alto_Navbar_FixedTop) + 'px)' });
          // $('.sidebar-wrapper .sidebar-footer').css('bottom', parseInt(Alto_Navbar_FixedTop)-5);
	});
	
    /** Igualar Anchos de Botones Registrarse y Autenticarse
    $(function(){
        var Ancho_btn_Autenticarse = $('.btn-autenticarse').css('width');
        $('.btn-registrarse').css('width', parseInt(Ancho_btn_Autenticarse) + "px !important");
    }); **/

    // Dropdown menu
    $(".sidebar-dropdown > a").click(function () {
        $(".sidebar-submenu").slideUp(200);
        if ($(this).parent().hasClass("active")) {
            $(".sidebar-dropdown").removeClass("active");
            $(this).parent().removeClass("active");
        } else {
            $(".sidebar-dropdown").removeClass("active");
            $(this).next(".sidebar-submenu").slideDown(200);
            $(this).parent().addClass("active");
        }

    });

    //toggle sidebar
    $("#toggle-sidebar").click(function () {
        $(".page-wrapper").toggleClass("toggled");
        $(".footer-general").toggleClass("toggled");
    });
    //Pin sidebar
    $("#pin-sidebar").click(function () {
        if ($(".page-wrapper").hasClass("pinned")) {
            // unpin sidebar when hovered
            $(".page-wrapper").removeClass("pinned");
            $("#sidebar").unbind( "hover");
        } else {
            $(".page-wrapper").addClass("pinned");
            $("#sidebar").hover(
                function () {
                    console.log("mouseenter");
                    $(".page-wrapper").addClass("sidebar-hovered");
                },
                function () {
                    console.log("mouseout");
                    $(".page-wrapper").removeClass("sidebar-hovered");
                }
            )

        }
    });


    //toggle sidebar overlay
    $("#overlay").click(function () {
        $(".page-wrapper").toggleClass("toggled");
    });

    //switch between themes 
    var themes = "default-theme legacy-theme chiller-theme ice-theme cool-theme light-theme amarillo-theme";
    $('[data-theme]').click(function () {
        $('[data-theme]').removeClass("selected");
        $(this).addClass("selected");
        $('.page-wrapper').removeClass(themes);
        $('.page-wrapper').addClass($(this).attr('data-theme'));
    });

    // switch between background images
    var bgs = "bg1 bg2 bg3 bg4";
    $('[data-bg]').click(function () {
        $('[data-bg]').removeClass("selected");
        $(this).addClass("selected");
        $('.page-wrapper').removeClass(bgs);
        $('.page-wrapper').addClass($(this).attr('data-bg'));
    });

    // toggle background image
    $("#toggle-bg").change(function (e) {
        e.preventDefault();
        $('.page-wrapper').toggleClass("sidebar-bg");
    });

    // toggle border radius
    $("#toggle-border-radius").change(function (e) {
        e.preventDefault();
        $('.page-wrapper').toggleClass("boder-radius-on");
    });

    //custom scroll bar is only used on desktop
    if (!/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        $(".sidebar-content").mCustomScrollbar({
            axis: "y",
            autoHideScrollbar: true,
            scrollInertia: 300
        });
        $(".sidebar-content").addClass("desktop");

    }

    $('.dropdown-submenu > a').on("click", function(e) {
    var submenu = $(this);
    $('.dropdown-submenu .dropdown-menu').removeClass('show');
    submenu.next('.dropdown-menu').addClass('show');
    e.stopPropagation();
    });

    $('.dropdown').on("hidden.bs.dropdown", function() {
        // hide any open menus when parent closes
        $('.dropdown-menu.show').removeClass('show');
    });


});