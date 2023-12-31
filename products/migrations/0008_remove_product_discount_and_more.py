# Generated by Django 4.2.6 on 2023-10-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_productimage_product_productimage_varient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='is_listed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
