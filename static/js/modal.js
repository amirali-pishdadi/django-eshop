function modal(modalId, btn, size = null) {
    var modal__id = $(modalId);
    var modal__btn = $(btn);
    var modal__content = modal__id.find('.modal__content').css('width', size);
    var modal__close = modal__id.find('.modal__close');
    modal__btn.click(function (e) {
        e.preventDefault();
        modal__id.css('display', 'block');
        $('body').css('overflow', 'hidden');
    });
    modal__close.click(function (e) {
        e.preventDefault();
        modal__id.css('display', 'none');
        $('body').css('overflow', 'unset');
    })

    $(document).on('click', function (e) {
        if (modal__id.is(e.target)) {
            modal__id.css('display', 'none');
            $('body').css('overflow', 'unset');
        }
    })
}

modal('#modal__gallery', '.gallery__slides')
$('.gallery__slide').click(function () {
    var getsrc = $(this).find('img').attr('src');
    $('.show__gallery').attr('src', getsrc);
})
