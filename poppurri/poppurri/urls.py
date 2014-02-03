#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: URL dispatcher configuration for project.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Translation support
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/rosetta/', include('rosetta.urls')),

    # Admin console
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Application views
    url(r'^contact/', include('contact_form.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^mixture/', include('mixture.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^$', include('web.urls')),
)


handler404 = 'web.views.not_found'
handler500 = 'web.views.server_error'


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns = patterns('',
        url(r'^404/$', handler404),
        url(r'^500/$', handler500),
    ) + urlpatterns

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        r'media/',
        document_root=settings.MEDIA_ROOT
    )

# vim: ai ts=4 sts=4 et sw=4 ft=python
