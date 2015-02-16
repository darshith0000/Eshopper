from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import make_password, User
from eshopper.accounts.forms import *
from shop.models import Order
from wishlist.models import WishlistItem


def account_select(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)

        if auth_form.is_valid():

            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['USER_ID'] = user.pk

                return HttpResponseRedirect(reverse('checkout'))

            else:
                messages.error(request, "Wrong username and Password combination.")
                return HttpResponseRedirect(reverse('account_login'))

        else:
            messages.error(request, "Wrong username and Password combination.")
            return HttpResponseRedirect('account_login')

    if request.method == 'GET':
        auth_form = AuthenticationForm()

        if request.session.get('USER_ID', ''):
            next = reverse('checkout')

            if next is not None:
                return HttpResponseRedirect(next)

        return render(request, "login.html", {
            'auth_form': auth_form,
        })


def account_signup(request):
    if request.method == 'GET':
        user_form = UserCreationForm()

        if request.session.get('USER_ID', ''):
            next = reverse('account_login')
            print next

            if next is not None:
                return HttpResponseRedirect(next)

        return render(request, "signup.html", {
            'user_form': user_form,
        })

    else:
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            data = user_form.data
            udata = {}

            if data['password1'] == data['password2']:
                try:
                    udata['username'] = data['username']
                    udata['password'] = make_password(data['password1'], salt="acc")
                    user = User.objects.create(**udata)

                    if user is not None:
                        user = authenticate(username=udata['username'], password=data['password1'])
                        login(request, user)
                        request.session['USER_ID'] = user.pk
                        return HttpResponseRedirect('/')

                except:
                    import sys
                    print sys.exc_value
                    messages.error(request, "Something went wrong. Please try again.")

        else:
            messages.error(request, "Please confirm your password.")
            return HttpResponseRedirect(reverse('signup'))


def show_form(request):
    if request.method == 'GET':
        user_form = UserCreationForm()
        auth_form = AuthenticationForm()

        if request.session.get('USER_ID', ''):
            next = reverse('account_login')

            if next is not None:
                return HttpResponseRedirect(next)

        return render(request, "signup.html", {
            'user_form': user_form,
            'auth_form': auth_form,
        })


def logout_view(request):
    logout(request)
    HttpResponseRedirect('account_login')
    # Redirect to a success page.

def account(request):
    orders = Order.objects.filter(user_id=request.user.id)
    wishlists = WishlistItem.objects.filter(user_id=request.user.id)
    return render(request, "accounts.html",{'orders':orders,'wishlists':wishlists})