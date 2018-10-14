$(document).ready(function () {
    let quantityBtn = $('.quantity-btn');
    let product = $('.product');
    let cartBtn = $('.to-cart');

    cartBtn.hover(function () {
        TweenMax.to($(this), 0.3, {scale: 1.2});
    }, function () {
        TweenMax.to($(this), 0.3, {scale: 1});
    });
    quantityBtn.mouseover(function () {
        if ($(this).hasClass('increase')){
            TweenMax.to($(this), 0.3, {scale: 1.2, backgroundColor: 'rgba(14, 194, 103, 0.7)'})
        }else{
            TweenMax.to($(this), 0.3, {scale: 1.2, backgroundColor: 'rgba(248, 36, 31, 0.7)'})
        }
    });
    quantityBtn.mouseout(function () {
        TweenMax.to($(this), 0.3, {scale: 1, backgroundColor: 'rgba(0, 0, 0, 0.2)'})
    });
    quantityBtn.click(function (e){
        e.preventDefault();
        let caption = $(this).closest('.product-caption');
        let input = caption.find('input');
        let value = Number(input.val());
        let price = Number(input.attr('price'));
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
   product.mouseover(function () {
        let product = $(this);
        TweenMax.to(product, 0.5, {
            background: 'linear-gradient(#FAFAFA, #FDFDFD, #FAFAFA)',
            boxShadow: '0 8px 16px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.23)',
            scale: 1.05,
            ease: Power1.easeInOut,
            zIndex: 50
        })
    });
    product.mouseleave(function () {
        let product = $(this);
        TweenMax.to(product, 0.5, {
            background: 'transparent',
            boxShadow: '0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)',
            scale: 1.0,
            ease: Power1.easeInOut,
            zIndex: 30
        })
    });
    cartBtn.click(function(e){
        e.preventDefault();
        let data = {};
        data['quantity'] = $(this).closest('.product-caption').find('input').val();
        data['id'] = $(this).attr('product-id');
        data['type'] = $(this).attr('product-type');
        let url = $(this).attr('url');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                let total = response['total'];
                let items = response['items'];
                let items_list = response['items_list'];
                $('.items').html(items);
                $('.total-price').html(total);
                let delete_url = $('#delete-header').attr('url');
                console.log(delete_url);
                let string = '';
                for (let i = 0; i <= items_list.length - 1; i++) {
                    x = items_list[i];
                    string += `
                    <tr>
                        <th class='name'>${x['name']}</th>
                        <th>${x['price']} &#8381;</th>
                        <th>${x['quantity']} ${x['unit']}</th>
                        <th>${x['subtotal']} &#8381;</th>
                    </tr>`;
                }
                $('.items-list').html(string);
                $('.add-popup').css('display', 'block');
                setTimeout(function () {
                    $('.add-popup')
                        .fadeOut()
                        .css('display', 'none');
                }, 1000);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});
