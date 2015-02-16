from django.contrib import admin
from models import Products


class ProductsAdmin(admin.ModelAdmin):
    display_fields = ["name", "category",]

admin.site.register(Products, ProductsAdmin)