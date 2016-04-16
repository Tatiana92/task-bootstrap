# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from news import views
import settings

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', views.get_news),
    url(r'^getall/$', views.get_news),
    url(r'^cat/(?P<cat_id>\d+)$', views.get_news),
    url(r'^vote/(?P<report_id>\d+)$', views.get_vote_template),
    url(r'^vote/setvote/$', views.set_vote),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
