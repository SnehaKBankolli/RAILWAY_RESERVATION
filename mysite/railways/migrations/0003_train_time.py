# Generated by Django 3.0.7 on 2020-06-12 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0002_auto_20200612_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 12, 12, 42, 39, 677918, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
