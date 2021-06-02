# Generated by Django 3.1.6 on 2021-05-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0007_auto_20210524_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='AmountofDonation',
            new_name='AmountofTip',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Submit',
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='ccode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='cdate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='cname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='cnum',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
