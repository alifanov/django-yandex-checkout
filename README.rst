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

4. Set up your webhook on Yandex Kassa profile page

5. Use ngrok or localtunnel to debug and test your project

Process payments responses
--------------------------

To process responses after paying you should use signals::

    from yandex_chekout.signals import payment_status_changed
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
        http://localhost:8000/yandex-checkut/payment-create/
    {
        'confirmation_url': 'https://...'
    }