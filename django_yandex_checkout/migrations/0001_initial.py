# Generated by Django 3.1.2 on 2020-10-25 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YandexKassaPayment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('period', models.CharField(default='month', max_length=255)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.PositiveIntegerField()),
                ('currency', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='yandex_kassa_payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
