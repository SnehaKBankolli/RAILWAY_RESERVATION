# Generated by Django 3.0.7 on 2020-06-12 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0003_train_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 12, 12, 43, 2, 879878, tzinfo=utc)),
            preserve_default=False,
        ),
    ]