# Generated by Django 3.1.2 on 2020-10-25 11:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20201019_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_PhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]