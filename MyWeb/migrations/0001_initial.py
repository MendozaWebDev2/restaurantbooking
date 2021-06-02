# Generated by Django 3.1.6 on 2021-05-15 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Name1', models.CharField(max_length=50, null=True)),
                ('Num', models.CharField(max_length=50, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('Submit', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AmountOfDonation', models.CharField(max_length=50, null=True)),
                ('Submit', models.CharField(max_length=50, null=True)),
                ('costumerId', models.ManyToManyField(to='MyWeb.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='DonateToAnimals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AmountofDonation', models.CharField(max_length=50, null=True)),
                ('Submit', models.CharField(max_length=50, null=True)),
                ('costumerId', models.ManyToManyField(to='MyWeb.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='BookingFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Submit', models.CharField(max_length=50, null=True)),
                ('costumerId', models.ManyToManyField(to='MyWeb.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rname', models.CharField(max_length=50, null=True)),
                ('Nums', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('Submit', models.CharField(max_length=50, null=True)),
                ('costumerId', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyWeb.booking')),
            ],
        ),
    ]
