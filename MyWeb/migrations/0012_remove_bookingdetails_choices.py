# Generated by Django 3.1.6 on 2021-06-12 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0011_auto_20210601_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdetails',
            name='Choices',
        ),
    ]
