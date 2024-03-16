$('.header__basket-icon').on('click', function () {
    $('.header__account .header__dropdown').removeClass('header__dropdown--is-active');
    $('.header__basket .header__dropdown').toggleClass('header__dropdown--is-active');
})
$('.header__account-icon').on('click', function () {
    $('.header__basket .header__dropdown').removeClass('header__dropdown--is-active');
    $('.header__account .header__dropdown').toggleClass('header__dropdown--is-active');
})
$('.btn--fav').on('click', function () {
    $(this).toggleClass('btn-fav--is-active');
})
$(document).on('click', function (e) {
    // console.log(e.target);
    // console.log($(e.target).closest('.header__basket,.header__account'));
    // console.log($(e.target).closest('.header__basket,.header__account').length);
    if (!$(e.target).closest('.header__basket,.header__account').length) {
        $('.header__dropdown').removeClass('header__dropdown--is-active')
    }
    if (!$(e.target).closest('.navbar').length) {
        $('.header__menu').removeClass('header__menu--is-active')
        $('.navbar__items').removeClass('navbar__items--is-active')
        $('.overlay').removeClass('overlay--is-active')
    }
})
$(window).scroll(function () {
    if ($(this).scrollTop() >= 200) {
        $('.scroll__top').fadeIn();
    } else {
        $('.scroll__top').fadeOut();
    }
})
$('.scroll__top').on('click', function () {
    $('html,body').animate({
        scrollTop: 0
    }, 800)
});
$('.header__menu').on('click', function () {
    $(this).toggleClass('header__menu--is-active');
    $('.navbar__items').toggleClass('navbar__items--is-active');
    $('.overlay').toggleClass('overlay--is-active');
});
$('.box__header').on('click', function () {
    var box_filter = $(this).parent().find('.box__filter');
    if ($(this).hasClass('box--togglable')) {
        $(this).removeClass('box--togglable');
        box_filter.slideDown();
    } else {
        $(this).addClass('box--togglable');
        box_filter.slideUp();
    }
});
$('.rating__rate').hover(function () {
    $('.rating__frate').addClass('rating__frate--is-acitve');
}, function () {
    $('.rating__frate').removeClass('rating__frate--is-acitve');
})
$('.rating__rate').on('click', function () {
    var data_width = $(this).data('width');
    console.log(data_width);
    $(this).parents('.rating').find('.rating__fstar').css('width', data_width);
})
$('.tab__item').on('click', function () {
    $('.tab__item').removeClass('tab__item--is-active');
    $(this).addClass('tab__item--is-active');
    var index = $(this).index();
    console.log(index);
    $('.tab__section').hide();
    $('.tab__section').eq(index).show();
})
$(document).ready(function () {
    $('.btn--reply[href^="#"]').on('click', function (e) {
        e.preventDefault();
        var target = this.hash;
        console.log(target);
        $('html,body').animate({
            'scrollTop': $(target).offset().top
        }, 800)
    })
})

function add_comment(product_id) {
    var message = document.getElementById("text_message").value
    $.get("/products/add_comment/", {
        product_id: product_id,
        message: message,
        parent_id: null,
    }).then(res => {
        document.getElementById("status").innerHTML = res.status
        document.getElementById("text_message").value = ""
    })

}

function removeCartItem(product_id) {
    $.get("/order/remove_product/?product_id=" + product_id).then(res => {
            swal.fire({
                    title: 'اعلان',
                    text: res.text,
                    icon: res.icon,
                    showCancelButton: false,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: res.confirm
                }
            )
        }
    )
    location.reload()
}

function add_to_order(product_id) {
    var count = document.getElementById("quantity").value
    console.log(count)
    if (count === "") {
        count = 1
    }
    console.log(count)
    $.get("/order/add_product/?count=" + count + "&product_id=" + product_id).then(res => {
            swal.fire({
                    title: 'اعلان',
                    text: res.text,
                    icon: res.icon,
                    showCancelButton: false,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: res.confirm
                }
            )
        }
    )
    location.reload()

}

function show_textarea() {
    var message = document.getElementById("text_message_pasokh").style.display = ""
    var pasokh = document.getElementById("button_pasokh").style.display = ""
    var text_message = document.getElementById("comments__send").style.display = 'none'
    // var text_message = document.getElementById("text_message").style.display = 'none'
    // var button_message = document.getElementById("button_message").style.display = 'none'

    }

function add_pasokh(product_id, parent_id) {
    var message = document.getElementById("text_message_pasokh").value
    $.get("/products/add_comment/", {
        product_id: product_id,
        message: message,
        parent_id: parent_id
    }).then(res => {
        console.log(product_id, message, parent_id)
        document.getElementById("status_pasokh").innerHTML = res.status
        document.getElementById("text_message_pasokh").value = ""
    })
}

function hidden_textarea() {
    var message = document.getElementById("text_message_pasokh").style.display = "none"
    var pasokh = document.getElementById("button_pasokh").style.display = "none"
}

function getBrands(brand_id) {

    console.log(brand_id)
    $.get("/products/all-product/?brand_id=" + brand_id)
    location.reload()
}
