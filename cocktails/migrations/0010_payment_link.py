# Generated by Django 4.0 on 2022-04-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_remove_payment_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
