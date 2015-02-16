from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def checkout(request):
    print "hello"
    return render(request, "shop/checkout/selection.html")
