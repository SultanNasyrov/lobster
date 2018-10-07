$(document).ready(function(){
	console.log('cart page js connected');
	$('.quantity-btn').click(function(){
		var unit = $(this).siblings('.unit').text();
		var quantity = $(this).siblings('.quantity');
		var value = Number(quantity.text());
		if ($(this).hasClass('increase')) {
			if (value == 15 || value == 1500){
				return;
			}else{
				var action = 'increase';
			}
		}else {
			if (value == 1 || value == 100){
				return;
			}else{
				var action = 'decrease';
			}
		}
		var total = $('.total-price');
		var subtotal = $(this).parent().parent().find('.subtotal')
		var url = $('.quantity-header').attr('url');
		var name = quantity.attr('name');
		data = {};
		data['name'] = name;
		data['unit'] = unit;
		data['action'] = action;
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			dataType: 'json',
			success: function (response) {
				console.log("success");
				quantity.html(response['quantity']);
				subtotal.html(response['subtotal']);
				total.html(response['total']);
		    },
		    error: function () {
				console.log('Error')
			}
		});
	});
	$('.delete').click(function(e){
		e.preventDefault();
		var name = $(this).attr('name');
		var url = $(this).attr('href');
		var line = $(this).parent().parent()
		data = {'name': name};
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			dataType: 'json',
			success: function (response) {
				console.log("success");
				$('.total-price').html(response['total']);
				$('.items').html(response['items']);
				line.remove();
		    },
		    error: function () {
				console.log('Error')
			}
		});
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
                $('.cart-table tbody').empty();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
	$('.order-btn').click(function(){
		$('.order-layout').css('display', 'flex');
	});
	$('.close').click(function(){
		$('.order-layout').css('display', 'none');
	});

	$(".phone-input").mask("+7 (999) 999-9999");

	$('.order').click(function(e){
		e.preventDefault();
		var form = $('.cart-form');
		var name = form.find('.name-input').val();
		var phone = form.find('.phone-input').val();
		var data = {'name': name, 'phone': phone};
		var url = form.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			dataType: 'json',
			success: function (response) {
				console.log("success");
		    },
		    error: function () {
				console.log('Error');
			}
		});
	});
})