# Generated by Django 2.2.8 on 2019-12-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=240)),
                ('patient', models.CharField(max_length=240)),
                ('message', models.TextField()),
            ],
        ),
    ]
