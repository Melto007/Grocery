# Generated by Django 3.1.1 on 2020-11-08 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0015_auto_20201108_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_cart',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='add_cart',
            name='user',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
