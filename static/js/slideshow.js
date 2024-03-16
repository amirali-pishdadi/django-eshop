var slideIndex = 1;
var items;
var time;
slideshow(slideIndex);

function slideshow(n) {
    console.log('slideIndex => ' + slideIndex);
    console.log('n => ' + n);
    var slides = document.getElementsByClassName('slideshow__slide')
    // var slides = $('.slideshow__slide');
    // console.log(slides);
    // $(slides).css('display', 'none');
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    console.log('slideIndex => ' + slideIndex);
    for (i = 0; i < slides.length; i++) {
        // console.log(i); // 0 1 2 3
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
    progress(slideIndex - 1);
}

function move(a) {
    clearInterval(time);
    items[slideIndex - 1].style.width = 0;
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

function progress(slideId) {
    items = document.getElementsByClassName('slideshow__item-inner');
    var width = 0;
    time = setInterval(timer, 10);

    // 10 * 100 = 1000;
    function timer() {
        if (width >= 100) {
            clearInterval(time);
            items[slideId].style.width = 0;
            slideIndex++;
            slideshow(slideIndex);
        } else {
            width++;
            items[slideId].style.width = width + "%";
        }
    }
}
