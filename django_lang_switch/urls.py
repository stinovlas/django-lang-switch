"""Urls module."""
from django.urls import include, path

app_name = 'django_lang_switch'
urlpatterns = [
    # Include set_language redirect view
    # https://docs.djangoproject.com/en/dev/topics/i18n/translation/#the-set-language-redirect-view
    path('i18n/', include('django.conf.urls.i18n')),
]
