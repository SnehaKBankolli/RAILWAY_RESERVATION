# Generated by Django 3.0.7 on 2020-06-12 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='time',
        ),
        migrations.RemoveField(
            model_name='train',
            name='time',
        ),
    ]