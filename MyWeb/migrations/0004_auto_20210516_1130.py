# Generated by Django 3.1.6 on 2021-05-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0003_auto_20210516_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='donatetoanimals',
            name='AmountofDonation',
            field=models.IntegerField(null=True),
        ),
    ]