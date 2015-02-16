from django.db import models
from django.contrib.admin import site
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.contrib import admin


class Address(models.Model):
    user_shipping = models.OneToOneField(User, related_name='shipping_address', blank=True, null=True)
    user_billing = models.OneToOneField(User, related_name='billing_address', blank=True, null=True)
