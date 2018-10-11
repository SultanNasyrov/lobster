$(document).ready(function () {

    // TODO interactive product cart elements
    $('.quantity-btn').click(function (e){
        e.preventDefault();
        var caption = $(this).closest('.product-caption');
        var input = caption.find('input');
        var value = Number(input.val());
        var price = Number(input.attr('price'));
        if (input.hasClass('number')) {
            if ($(this).hasClass('increase') && value < 15) {
                value += 1;
                input.val(value);
                price *= value;
                caption.find('.price').html(price);
            }else if($(this).hasClass('decrease') && value >= 2){
                value -= 1;
                input.val(value);
                price *= value;
                caption.find('.price').html(price);
            }
        }else {
            if ($(this).hasClass('increase') && value < 1500) {
                value += 100;
                input.val(value);
                price *= value / 100;
                caption.find('.price').html(price);
            }else if($(this).hasClass('decrease') && value >= 200){
                value -= 100;
                input.val(value);
                price *= value / 100;
                caption.find('.price').html(price);
            }
        }
    });
    $('.product').mouseover(function () {
        var product = $(this);
        TweenMax.to(product, 0.5, {
            background: 'linear-gradient(#FAFAFA, #FDFDFD, #FAFAFA)',
            boxShadow: '0 8px 16px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.23)',
            scale: 1.05,
            ease: Power1.easeInOut,
            zIndex: 50
        })
    });
    $('.product').mouseleave(function () {
        var product = $(this);
        TweenMax.to(product, 0.5, {
            background: 'transparent',
            boxShadow: '0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)',
            scale: 1.0,
            ease: Power1.easeInOut,
            zIndex: 30
        })
    });
    $('.to-cart').click(function(e){
        e.preventDefault();
        var data = {};
        data['quantity'] = $(this).closest('.product-caption').find('input').val();
        data['id'] = $(this).attr('product-id');
        data['type'] = $(this).attr('product-type');
        var url = $(this).attr('url');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                var total = response['total'];
                var items = response['items'];
                var items_list = response['items_list'];
                $('.items').html(items);
                $('.total-price').html(total);
                var delete_url = $('#delete-header').attr('url');
                console.log(delete_url);
                var string = ''
                for (var i = 0; i <= items_list.length - 1; i++) {
                    x = items_list[i]
                    var new_string = `
                    <tr>
                        <th class='name'>${x['name']}</th>
                        <th>${x['price']} &#8381;</th>
                        <th>${x['quantity']} ${x['unit']}</th>
                        <th>${x['subtotal']} &#8381;</th>
                  </tr>`
                    string += new_string;
                }
                $('.items-list').html(string);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
})
