# Generated by Django 3.0.7 on 2020-06-12 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0004_ticket_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
