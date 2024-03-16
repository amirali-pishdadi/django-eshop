
$(document).ready(function () {
    $('.slider').each(function () {
        var swiper = $(this).find('.swiper-container');
        var slider__content = $(this).find('.slider__content');
        var swiper_button_next = slider__content.next();
        var swiper_button_prev = swiper_button_next.next();
        new Swiper(swiper, {
            loop: false,
            nextButton: swiper_button_next,
            prevButton: swiper_button_prev,
            slidesPerView: 4,
            paginationClickable: true,
            spaceBetween: 20,
            breakpoints: {
                1920: {slidesPerView: 4, spaceBetween: 20},
                1028: {slidesPerView: 3, spaceBetween: 20},
                768: {slidesPerView: 2, spaceBetween: 10},
                480: {slidesPerView: 1, spaceBetween: 0},
            }
        })
    })

});