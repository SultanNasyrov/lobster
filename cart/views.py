from django.shortcuts import render, HttpResponse, Http404
from .cart import Cart
import json

# Create your views here.

def cart(request):

    context = {
    }
    return render(request, 'cart.html', context)

def add_item(request):

    if request.method == 'POST' and request.is_ajax():
        print('Adding item ... ')
        product_id = request.POST['id']
        product_type = request.POST['type']
        quantity = request.POST['quantity']
        cart = Cart(request)
        cart.add_item(request, id=product_id, type=product_type, quantity=quantity)
        total = cart.total()
        items = cart.items_count()
        items_list = cart.items_list()
        print(items_list)
        response = {
            'total': total,
            'items': items,
            'items_list': items_list
        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def clean_cart(request):
    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        cart.clean_cart(request)
        response = {'result': 'ok'}
        return HttpResponse(json.dumps(response))
    else: 
        raise Http404

    print('cleaning cart ... ')
    cart = Cart(request)
    cart.clean_cart(request)
    response = {'result': 'ok'}
    return HttpResponse(json.dumps(response))


def delete_item(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        cart = Cart(request)
        cart.delete_item(request, name)
        total = cart.total()
        items = cart.items_count()
        response = {
            'total': total,
            'items': items,
        }
        return HttpResponse(json.dumps(response))
    else: 
        raise Http404

def change_quantity(request):
    
    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        unit = request.POST['unit']
        action = request.POST['action']
        print(name, unit, action)
        cart = Cart(request)
        result = cart.change_quantity(request, name, unit, action)

        response = {
            'subtotal': result[0],
            'quantity': result[1],
            'total': cart.total(),

        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def order(request):

    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        phone = request.POST['phone']
        cart = Cart(request)
        cart.make_order(request, name, phone)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404