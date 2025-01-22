from django.contrib import admin # type: ignore
from .models import Category, Customer, Product, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
