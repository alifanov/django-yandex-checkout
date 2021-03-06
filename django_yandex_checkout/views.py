import json
import uuid

from datetime import datetime, timedelta

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from yandex_checkout import Configuration, Payment

from django.conf import settings
from django.http import JsonResponse

from .models import *
from .signals import *

Configuration.account_id = settings.YANDEX_KASSA_SHOP_ID
Configuration.secret_key = settings.YANDEX_KASSA_SECRET_KEY

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def yandex_kassa_webhook_handler(request):
    payment_id = request.data['object']['id']
    status = request.data['object']['status']

    ykp = YandexKassaPayment.objects.filter(id=payment_id).first()
    if ykp:
        if ykp.status != status:
            payment_status_changed.send(sender=YandexKassaPayment, status=status, data=data)

        ykp.status = status
        ykp.save()
    return JsonResponse({})


@api_view(['POST'])
def create_payment(request):
    if not 'payment_total_sum' in request.data:
        return JsonResponse({'error': 'payment_total_sum not found in parameters'})

    payment_total_sum = request.data['payment_total_sum']
    payment = Payment.create({
            "amount": {
            "value": payment_total_sum,
            "currency": 'RUB'
        },
        "confirmation": {
            "type": "redirect",
            "return_url": settings.YANDEX_KASSA_RETURN_URL
        },
        "capture": True,
    }, uuid.uuid4())
    ykp = YandexKassaPayment.objects.create(
        id=payment.id,
        user=request.user,
        status=payment.status,
        description=payment.description,
        value=payment.amount.value,
        currency=payment.amount.currency
    )
    return JsonResponse({
        'confirmation_url': payment.confirmation.confirmation_url
    })