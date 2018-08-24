"""Tests settings."""

SECRET_KEY = 'Chamber of secrets'

INSTALLED_APPS = [
    'django_lang_switch.apps.DjangoLangSwitchConfig',
]

ROOT_URLCONF = 'django_lang_switch.tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
