# Generated by Django 3.1.1 on 2020-11-08 09:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0014_auto_20201108_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_cart',
            name='foods',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='foods',
            field=models.ManyToManyField(blank=True, null=True, to='store.Foods'),
        ),
        migrations.RemoveField(
            model_name='add_cart',
            name='user',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
