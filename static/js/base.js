$(document).ready(function () {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    $('.cart').mouseover(function () {
        var cart = $(this);
        var items = $(this).find('.cart-items');
        TweenMax.to(items, 0.5, {display: 'flex'});
    });
    $('.cart').mouseout(function () {
        var cart = $(this);
        var items = $(this).find('.cart-items');
        TweenMax.to(items, 0.1, {display: 'none'});
    });
    $('.clean').click(function (e) {
        e.preventDefault();
        var data = {};
        var url = $(this).attr("href");
        console.log(url);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                $('.items').html(0);
                $('.total-price').html(0);
                $('.items-list').empty();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    
});