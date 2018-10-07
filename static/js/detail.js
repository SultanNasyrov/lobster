$(document).ready(function () {
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
                console.log("success");
                console.log('server answered ', response['result']);
            },
            error: function () {
                console.log('Error')
            }
        });
    });
    $('.cart-btn').click(function (e) {
        e.preventDefault();

        var data = {};
        var url = $('form').attr('action');
        data['id'] = Number($('form').attr('target-id'));
        data['type'] = $('form').attr('target-type');
        data['quantity'] = $('form').find('.number-field').val();
        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
                var result = response['result'];
                console.log('ajax response ', result);
            },
            error: function () {
                console.log('Error')
            }
        });
    });
});


