$('.gallery__slide').each(function (i) {
    var img__src = $(this).find('img').attr('src');
    // console.log(img__src);
    var createItem = '<div class="gallery__item"><img src="' + img__src + '" onclick="currentSlide(' + (i + 1) + ')" class="gallery__item-img"></div>';
    $('.gallery__items').append(createItem);

})

var slideIndex = 1;
slideshow(slideIndex);

function slideshow(n) {
    var slides = document.getElementsByClassName('gallery__slide')
    $('.gallery__number2').text(slides.length)
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    $('.gallery__number1').text(slideIndex)
    for (i = 0; i < slides.length; i++) {
        // console.log(i); // 0 1 2 3
        slides[i].style.display = "none";
    }
    var gallery__item = $('.gallery__item');
    $(gallery__item).removeClass('gallery__item--is-acitve');
    slides[slideIndex - 1].style.display = "block";
    $(gallery__item[slideIndex -1]).addClass('gallery__item--is-acitve');

}

function move(a) {
    //slidexIndex --> 1 | 2 | 3 | 4
    //Next ---> 1
    //slideIndex = 5 + 1 = 5
    //-----------prev--------
    //slideIndex ---> 4 | 3 | 2 | 1
    //prev ---> -1
    // slideIndex =1 + -1 --> (+-)= - ---> 1 - 1 = 0
    slideIndex = slideIndex + a; // slideIndex 1 -->prev -1  1 + -1= 1-1=0
    slideshow(slideIndex);
}

function currentSlide(n) {
    slideshow(slideIndex = n)
}