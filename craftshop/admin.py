from django.contrib import admin
from .models import Beer, Snack, SnackCategory, Order, OrderItem


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    pass


@admin.register(SnackCategory)
class SnackCategoryAdmin(admin.ModelAdmin):
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

