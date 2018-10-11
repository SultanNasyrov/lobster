from craftshop.models import Snack, Beer, Order, OrderItem
from django.shortcuts import get_object_or_404


class CartItem(object):
    """Cart item

    constructs  cart item instance.

    """
    def __init__(self, id, quantity, type):
        if type == 'beer':
            product = get_object_or_404(Beer, id=id)
            self.unit = 'л'
            subtotal = int(product.price) * int(quantity)
            self.type = 'beer'
        else:
            product = get_object_or_404(Snack, id=id)
            self.type = 'snack'
            if product.packed:
                x = int(quantity) / 100
                subtotal = int(product.price) * int(x)
                self.unit = 'гр'
            else:
                subtotal = int(product.price) * int(quantity)
                self.unit = 'шт'
        self.id = int(id)
        self.name = str(product.name)
        self.price = int(product.price)
        self.quantity = int(quantity)
        self.subtotal = subtotal

    def make_dict(self):
        """returns dictionary object ready to be serialised in sessions"""
        item = {
            'type': self.type,
            'name': self.name,
            'id': self.id,
            'price': self.price,
            'quantity': self.quantity,
            'subtotal': self.subtotal,
            'unit': self.unit}
        return item


class Cart(object):
    """Cart object

        Manages cart and cart items stored in sessions

    """
    def __init__(self, request):
        """test whether cart is in the sessions. If not creates a dict a puts it there"""
        if 'cart' in request.session:
            self.cart = request.session['cart']
        else:
            print('cart is not in the session')
            self.cart = {}
            request.session['cart'] = self.cart

    def save_changes(self, request):
        """saves current self cart instance in the session"""
        request.session['cart'] = self.cart
        print('Cart saved')

    def items_list(self):
        """return current cart list of items"""
        items_list = list(self.cart.values())
        return items_list

    def items_count(self):
        """return number of items stored in current cart"""
        return len(self.cart)

    def add_item(self, request, id, type, quantity=1):
        """

        adds items to the cart.
        if item already exists adds quantity and counts subtotal

        """
        item = CartItem(id=id, quantity=quantity, type=type)
        name = item.name
        if name in self.cart:
            price = self.cart[name]['price']
            self.cart[name]['quantity'] += int(quantity)
            new_quantity = self.cart[name]['quantity']
            if item.unit == 'гр':
                self.cart[name]['subtotal'] = price * int(new_quantity / 100)
            else:
                self.cart[name]['subtotal'] = price * int(new_quantity)
        else:
            self.cart[name] = item.make_dict()
        self.save_changes(request)

    def delete_item(self, request, name):
        """deletes item by the name"""
        key = str(name)
        self.cart.pop(key)
        self.save_changes(request)

    def clean_cart(self, request):
        """Deletes all items """
        self.cart.clear()
        self.save_changes(request)

    def change_quantity(self, request, name, unit, action):
        """changes quantity of item in cart"""
        key = str(name)
        if action == 'increase':
            if unit == 'гр':
                self.cart[key]['quantity'] += 100
            else:
                self.cart[key]['quantity'] += 1
            self.cart[key]['subtotal'] += int(self.cart[key]['price'])
        else:
            if unit == 'гр':
                self.cart[key]['quantity'] -= 100
            else:
                self.cart[key]['quantity'] -= 1
            self.cart[key]['subtotal'] -= int(self.cart[key]['price'])
        self.save_changes(request)
        new_subtotal = self.cart[key]['subtotal']
        new_quantity = self.cart[key]['quantity']
        return [new_subtotal, new_quantity]

    def total(self):
        """Counts total cart price"""
        prices = []
        for item in self.cart.values():
            price = item['subtotal']
            prices.append(price)
        total = 0
        for item in prices:
            total += int(item)
        return total

    def make_order(self, request, name, phone):
        """makes Order model instance from session cart.

            creates Order model instance
            creates associated with Order OrderItem instances
            for all session cart items stored there
            saves Order and cleans session cart

        """
        total = self.total()
        order = Order.objects.create(name=name, phone=phone, total=total)

        for x in self.items_list():
            OrderItem.objects.create(order=order, name=x['name'], price=x['price'],
                                     quantity=x['quantity'], subtotal=x['subtotal'])
        self.clean_cart(request)

