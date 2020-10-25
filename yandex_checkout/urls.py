from django.contrib import admin
from django.urls import path

from .views import create_payment, yandex_kassa_webhook_handler

urlpatterns = [
    path('yandex-checkout/payment-create/', create_payment, name='create_payment'),
    path('yandex-checkout/webhook/', yandex_kassa_webhook_handler, name='yandex_kassa_webhook_handler'),
]
