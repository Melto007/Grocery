# Generated by Django 3.1.1 on 2020-11-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20201108_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_cart',
            name='user',
        ),
        migrations.AddField(
            model_name='add_cart',
            name='foods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.foods'),
        ),
    ]