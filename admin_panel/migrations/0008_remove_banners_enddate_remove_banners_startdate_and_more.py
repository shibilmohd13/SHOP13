# Generated by Django 4.2.6 on 2023-11-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_banners_enddate_alter_banners_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banners',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='banners',
            name='startdate',
        ),
        migrations.AddField(
            model_name='banners',
            name='is_listed',
            field=models.BooleanField(default=True),
        ),
    ]
