# Generated by Django 4.2.6 on 2023-11-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_ordersitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='ORD7801a2', editable=False, max_length=12, primary_key=True, serialize=False),
        ),
    ]