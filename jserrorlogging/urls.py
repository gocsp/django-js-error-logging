# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns
from .views import LoggingView

from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns(
    '',
    url(r'^add/$', csrf_exempt(LoggingView.as_view()), name='add_log'),
)
