from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from shop import urls as shop_urls

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^accounts/', include('eshopper.accounts.urls')),
    # url(r'', include('password_reset.urls')),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^checkout/', 'eshopper.views.checkout', name='checkout'),
    url(r'^shop/', include(shop_urls)),
    url(r'^wishlist/', include('wishlist.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls'), ),
)