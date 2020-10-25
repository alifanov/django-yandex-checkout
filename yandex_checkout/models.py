import uuid

from django.db import models
from django.conf import settings

# Create your models here.
class YandexKassaPayment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_WAITING_FOR_CAPTURE = 'waiting_for_capture'
    STATUS_SUCCEEDED = 'succeeded'
    STATUS_CANCELED = 'canceled'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='yandex_kassa_payments'
    )
    period = models.CharField(default='month', max_length=255)
    status = models.CharField(max_length=255, default='pending')
    description = models.TextField(blank=True, null=True)
    value = models.PositiveIntegerField()
    currency = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)