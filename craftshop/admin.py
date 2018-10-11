from django.contrib import admin
from .models import Beer, Snack, Order, OrderItem, Combo
# TODO write comments in admin page
# TODO customize admin page
# TODO customize visual admin page


@admin.register(Combo)
class CombeAdmin(admin.ModelAdmin):
    pass


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['name', 'price', 'quantity', 'subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    inlines = [OrderItemInline]
    readonly_fields = ['name', 'phone', 'total', 'date']
    list_display = ['name', 'phone', 'total', 'date']

