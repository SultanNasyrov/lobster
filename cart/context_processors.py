from cart.cart import Cart


def cart(request):
    """return cart in the """
    cart = Cart(request)
    context = {
        'items': cart.items_count(),
        'cart': cart.items_list(),
        'total': cart.total(),
    }
    return context