from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
        # url(r'^loginpage/$','eshopper.accounts.views.account_select',name='login'),
        url(r'^login/$','eshopper.accounts.views.account_select',name='account_login'),
        url(r'^signup_filled/$','eshopper.accounts.views.account_signup',name='account_signup'),
        url(r'^signup/$','eshopper.accounts.views.show_form',name='signup'),
        url(r'^logout$', 'django.contrib.auth.views.logout', {"next_page": "/en/"}, name='logout'),
        url(r'^$','eshopper.accounts.views.account', name='account'),
        url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
        url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
        url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
        url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)