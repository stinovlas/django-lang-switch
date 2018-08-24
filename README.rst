==================
django-lang-switch
==================

.. image:: https://travis-ci.org/stinovlas/django-lang-switch.svg?branch=devel
    :target: https://travis-ci.org/stinovlas/django-lang-switch/branches
.. image:: https://codecov.io/gh/stinovlas/django-lang-switch/branch/devel/graph/badge.svg
    :target: https://codecov.io/gh/stinovlas/django-lang-switch/branch/devel
.. image:: https://img.shields.io/pypi/v/django-lang-switch.svg
    :target: https://pypi.org/project/django-lang-switch
.. image:: https://img.shields.io/pypi/pyversions/django-lang-switch.svg
    :target: https://pypi.org/project/django-lang-switch
.. image:: https://img.shields.io/pypi/djversions/django-lang-switch.svg
    :target: https://pypi.org/project/django-lang-switch

Language switch for Django.


--------------
 Installation
--------------

You can install ``django-lang-switch`` from PyPi:

.. code-block:: bash

    $ pip install django-lang-switch


---------------
 Configuration
---------------

You need to add ``django_lang_switch.apps.DjangoLangSwitchConfig`` into your ``INSTALLED_APPS`` setting.
If you want to add enable language switch in django admin site, you have to add it before ``django.contrib.admin``.
Otherwise, you need to put ``django.contrib.admin`` first.
If you don't use django admin site, the order does not matter.

If you tweaked the ``admin/base_site.html`` template yourself,
put this application after yours and use the template tag as described below.

You also need to include ``django-lang-switch`` urls to your ``ROOT_URLCONF``. Example:

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        ...
        path('django_lang_switch/', include('django_lang_switch.urls')),
    ]

You can of course change the path to suit your needs.


-------
 Usage
-------

If you just want to add language switch to django admin site,
add this application to your ``INSTALLED_APPS`` as described above and you are done.

If you want to use the same switch elsewhere, add template tage ``lang_switch_dropdown`` to your template.
Don't forget to load ``lang_switch`` tag collection to your template. Example:

.. code-block:: html

    {% extends myapp/base_site.html %}
    {% load lang_switch %}
    <div id="header">
        Welcome to MyApp!
        <div class="right">
            {% lang_switch_dropdown %}
        </div>
    </div>


---------
 Styling
---------

Language switch in django admin site is already styled to fit the default design.
If you want to style the lang switch yourselves,
you may set css for the ``div.lang-switch`` element and its descendants.
