# Generated by Django 3.1.6 on 2021-05-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0002_remove_ratings_amountofdonation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Num',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='date',
            field=models.DateTimeField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='time',
            field=models.TimeField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donatetoanimals',
            name='AmountofDonation',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
