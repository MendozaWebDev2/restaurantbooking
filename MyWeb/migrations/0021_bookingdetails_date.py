# Generated by Django 3.1.6 on 2021-06-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0020_auto_20210623_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
