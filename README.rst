=====
django-yandex-checkout
=====

django-yandex-checkout is a Django app to process payments with Yandex Kassa

Quick start
-----------

1. Add "django_yandex_checkout" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_yandex_checkout',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('django_yandex_checkout/', include('django_yandex_checkout.urls')),

3. Run ``python manage.py migrate`` to create the django_yandex_checkout models.

4. Set up your webhook on Yandex Kassa profile page

5. Use ngrok or localtunnel to debug and test your project