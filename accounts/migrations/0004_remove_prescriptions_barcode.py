# Generated by Django 2.2.8 on 2019-12-22 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_prescriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescriptions',
            name='barcode',
        ),
    ]
