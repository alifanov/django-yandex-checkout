======================
django-yandex-checkout
======================

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

4. Add settings in settings.py::

    YANDEX_KASSA_SHOP_ID = '...'
    YANDEX_KASSA_SECRET_KEY = '...'
    YANDEX_KASSA_RETURN_URL = '...'

5. Set up your webhook on Yandex Kassa profile page

6. Use ngrok or localtunnel to debug and test your project

Process payments responses
--------------------------

To process responses after paying you should use signals::

    from django_yandex_checkout.signals import payment_status_changed
    from django.dispatch import receiver

    @receiver(payment_status_changed)
    def my_callback(sender, **kwargs):
        print("Payment status changed!")

Create payment
--------------

To create payment use POST query::

    curl  -X POST \
          -H "Content-Type: application/json"\
          -d '{"payment_total_sum": 100.0}'\
        http://localhost:8000/yandex-checkout/payment-create/
    {
        'confirmation_url': 'https://...'
    }