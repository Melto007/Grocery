# Generated by Django 3.1.1 on 2020-11-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20201108_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]