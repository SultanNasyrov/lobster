$(document).ready(function () {
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
    })
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
