# Generated by Django 3.1.6 on 2021-05-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0006_auto_20210517_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AmountofDonation', models.IntegerField(null=True)),
                ('costumerId', models.ManyToManyField(to='MyWeb.Booking')),
            ],
        ),
        migrations.RemoveField(
            model_name='donatetoanimals',
            name='costumerId',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='Submit',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='Submit',
        ),
        migrations.DeleteModel(
            name='BookingFee',
        ),
        migrations.DeleteModel(
            name='DonateToAnimals',
        ),
    ]
