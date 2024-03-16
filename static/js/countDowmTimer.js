function countDowmTimer() {
    var countDown = $('.count-down__timer');
    var countDownDate = new Date(countDown.data('countdown')).getTime();

    var timer = setInterval(function () {
        var now = new Date().getTime();
        var distance = countDownDate - now;

        var days = Math.floor(
            distance / (1000 * 60 * 60 * 24)
        );
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        // (10 mod (20 * 20)) / (2 * 5)
        // 20 * 20 = 400
        // 10 mod 400 = 10
        // 2 * 5 = 10
        //10 / 10 = 1
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000)
        // (10 mod (10 * 10 )) /10
        // 10 * 10 = 100
        // 10 mod 100 = 10
        // 10 /10 = 1
        countDown.html(days + ':' + hours + ":" + minutes + ':' + seconds)
        if (distance <= 0) {
            clearInterval(timer);
            $('.product__expiration').hide();
        }
    }, 0)
}

countDowmTimer();