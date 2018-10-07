from craftshop.models import Snack, Beer, Order, OrderItem
from django.shortcuts import get_object_or_404


class CartItem(object):

    def __init__(self, id, quantity, type):

        if type == 'beer':
            product = get_object_or_404(Beer, id=id)
            self.unit = 'л'
            subtotal = int(product.price) * int(quantity)
            self.type = 'beer'

        else:
            product = get_object_or_404(Snack, id=id)
            self.type = 'snack'
            if product.packing == True:
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

    def __init__(self, request):

        if 'cart' in request.session:
            self.cart = request.session['cart']
        else:
            print('cart is not in the session')
            self.cart = {}
            request.session['cart'] = self.cart

    def save_changes(self, request):
        request.session['cart'] = self.cart
        print('Cart saved')

    def items_list(self):
        items_list = list(self.cart.values())
        return items_list

    def items_count(self):
        return len(self.cart)

    def add_item(self, request, id, type, quantity=1):

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
        print('deleting started')
        print('#' * 50)
        print('cart before deleting')
        print(self.cart)
        print('#' * 50)
        key = str(name)
        print('key is', key)
        print('start deleting')
        self.cart.pop(key)
        print('#' * 50)
        print('cart after deleting')
        print(self.cart)
        self.save_changes(request)

    def clean_cart(self, request):
        self.cart.clear()
        self.save_changes(request)

    def change_quantity(self, request, name, unit, action):
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
        prices = []
        for item in self.cart.values():
            price = item['subtotal']
            prices.append(price)
        total = 0
        for item in prices:
            total += int(item)
        return total

    def make_order(self, request, name, phone):
        
        total = self.total()
        order = Order.objects.create(name=name, phone=phone, total=total)

        for x in self.items_list():
            item = OrderItem.objects.create(order=order, name=x['name'], price=x['price'],
                                            quantity=x['quantity'], subtotal=x['subtotal'])
        self.clean_cart(request)

