"""Tests url dispatcher."""
from django.urls import include, path

urlpatterns = [
    path('django_lang_switch/', include('django_lang_switch.urls')),
]
