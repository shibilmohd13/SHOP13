# Generated by Django 4.2.6 on 2023-11-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_address_is_primary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='is_primary',
        ),
        migrations.AddField(
            model_name='address',
            name='is_present',
            field=models.BooleanField(default=True),
        ),
    ]
