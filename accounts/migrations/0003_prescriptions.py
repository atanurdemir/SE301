# Generated by Django 2.2.8 on 2019-12-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=50)),
                ('diagnosis', models.CharField(max_length=50)),
                ('recipe', models.TextField()),
                ('barcode', models.CharField(blank=True, default='4961389914', editable=False, max_length=10, unique=True)),
            ],
        ),
    ]