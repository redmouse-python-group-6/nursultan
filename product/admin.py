from __future__ import unicode_literals

from django.contrib import admin
from product.models import Product, Category


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_date_update']
    list_display = ['product_name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title']
    fields = ['category_title', 'category_parent']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)