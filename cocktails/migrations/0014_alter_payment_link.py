# Generated by Django 4.0 on 2022-04-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0013_rename_payment_order_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
