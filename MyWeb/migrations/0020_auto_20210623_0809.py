# Generated by Django 3.1.6 on 2021-06-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0019_remove_bookingdetails_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdetails',
            name='date',
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='time',
            field=models.TimeField(max_length=50, null=True),
        ),
    ]