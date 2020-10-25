import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User

from unittest.mock import patch

from .models import *

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

# Create your tests here.
class APITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    @patch('yandex_checkout.Payment.create')
    def test_create_payment(self, mocked_payment_create):
        class PaymentMock:
            id=1
            status = 'pending'
            description = 'test desciption'
            amount = dotdict({'value': 1, 'currency': 'RUB'})
            confirmation = dotdict({'confirmation_url': 'http://confirmation_url'})

        mocked_payment_create.return_value = PaymentMock()

        data = {'payment_total_sum': 100.0}
        self.client.login(username='jacob', password='top_secret')

        self.assertEqual(YandexKassaPayment.objects.count(), 0)
        resp = self.client.post(reverse('create_payment'), json.dumps(data), content_type="application/json")
        self.assertTrue(resp.status_code, 200)
        self.assertEqual(YandexKassaPayment.objects.count(), 1)