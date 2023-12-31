# Generated by Django 4.2.6 on 2023-11-28 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_alter_banners_enddate_alter_banners_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 19, 4, 57, 902546)),
        ),
        migrations.AlterField(
            model_name='banners',
            name='image',
            field=models.ImageField(height_field='500px', upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 19, 4, 57, 902546)),
        ),
    ]
