# Generated by Django 3.1.6 on 2021-06-23 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0017_auto_20210622_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='Nums',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
