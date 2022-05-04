# Generated by Django 4.0 on 2022-04-22 10:08

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0029_order_orderid_alter_order_ordered_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 12, 8, 53, 934578)),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.UUIDField(db_index=True, default=uuid.uuid1, editable=False, unique=True),
        ),
    ]
