# Generated by Django 4.0 on 2022-04-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0024_remove_orderitem_order_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ordered',
            field=models.ManyToManyField(blank=True, to='cocktails.OrderItem'),
        ),
    ]
