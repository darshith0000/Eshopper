from shop.models import Product
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Products(Product):
    category = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='static/images', null=True)

    class Meta(object):
        verbose_name = _('Products')
        verbose_name_plural = _('Products')

