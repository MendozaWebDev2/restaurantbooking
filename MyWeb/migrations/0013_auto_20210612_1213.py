# Generated by Django 3.1.6 on 2021-06-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0012_remove_bookingdetails_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='Kind',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tip',
            name='add',
            field=models.IntegerField(null=True),
        ),
    ]