# Generated by Django 4.1.3 on 2024-04-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0004_payment_created_at_payment_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='isdelivered',
            field=models.BooleanField(default=False),
        ),
    ]
