# Generated by Django 3.1.1 on 2020-11-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20201108_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_cart',
            old_name='food_id',
            new_name='foods',
        ),
        migrations.RenameField(
            model_name='add_cart',
            old_name='customer_id',
            new_name='user',
        ),
    ]