# Generated by Django 3.1.6 on 2021-05-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0008_auto_20210528_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='Choices',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='rate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]