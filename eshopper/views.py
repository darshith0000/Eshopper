__author__ = 'darshithb'

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.conf.urls import patterns, url
from django.shortcuts import render
from shop.util.decorators import on_method, shop_login_required, order_required
from shop.models import Order, OrderItem, Cart


def checkout(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('checkout_selection'))
    else:
        return HttpResponseRedirect('/accounts/login')


class BaseShipping(object):
    """
    This is a simple free shipping backend that sets the shipping cost to 0
    and makes the shipping component of checkout invisible to the user
    """
    url_namespace = 'shipping'
    backend_name = 'Base shipping'

    def __init__(self, shop):
        self.shop = shop
        self.rate = 0
        self.rates_dict = {}

    @on_method(shop_login_required)
    @on_method(order_required)
    def select_method(self, request):
        cart = Cart.objects.filter(user_id=request.user.id)[0]
        order = Order.objects.filter(cart_pk=cart.id).order_by('-created')[0]
        address_ship = order.shipping_address_text
        address_bill = order.billing_address_text
        list_ship = [x.strip() for x in address_ship.split(',')]
        list_bill = [x.strip() for x in address_bill.split(',')]
        order_items = OrderItem.objects.filter(order_id=order.id)
        context = order_items
        return render(request, "shop/checkout/order_details.html", {'order_items': context, 'order': order,
                                                               'list_b': list_bill, 'list_s': list_ship})

    @on_method(shop_login_required)
    @on_method(order_required)
    def view_process_order(self, request):
        """
        A simple (not class-based) view to process an order.

        This will be called by the selection view (from the template) to do the
        actual processing of the order (the previous view displayed a summary).

        It calls shop.finished() to go to the next step in the checkout
        process.
        """
        service_method = request.POST.get('method')
        self.rate = self.rates_dict.get(service_method, 0)
        request.session['shipping_charge'] = self.rate
        self.shop.add_shipping_costs(self.shop.get_order(request),
                                     service_method,
                                     Decimal(self.rate))
        return self.shop.finished(self.shop.get_order(request))

    def get_urls(self):
        """
        Return the list of URLs defined here.
        """
        urlpatterns = patterns('',
            url(r'^$', self.select_method, name="shipping"),
            url(r'^complete/$', self.view_process_order, name="shipping_method"),
        )
        return urlpatterns