# Generated by Django 3.1.1 on 2020-11-07 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0010_auto_20201107_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_cart',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='add_cart',
            name='food_id',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='food_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.foods'),
        ),
    ]