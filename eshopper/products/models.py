# from django.db import models
# from shop.models import Product
# from django.contrib import admin
#
# class Products(Product):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     category = models.CharField(max_length=255, blank=True, null=True)
#     unit_price = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         pass
# #
# # class ProductsAdmin(admin.ModelAdmin):
# #     list_display = ('name','category',)
# #     list_filter = ('category',)
# #     search_fields = ('name',)
# #
# # admin.site.register(Products, ProductsAdmin)