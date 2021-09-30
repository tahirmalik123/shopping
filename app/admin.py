from django.contrib import admin
from .models import Product, Customer, Cart, Order_Placed


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zip_code', 'state']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discount_price', 'city', 'description', 'brand', 'catagory', 'image']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']

@admin.register(Order_Placed)
class order_placedAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'customer', 'product', 'quantity', 'ordered_date', 'status']