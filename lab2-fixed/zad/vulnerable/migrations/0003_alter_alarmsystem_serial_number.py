# Generated by Django 4.0 on 2021-12-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerable', '0002_alarmsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmsystem',
            name='serial_number',
            field=models.IntegerField(),
        ),
    ]