# Generated by Django 4.2.5 on 2023-09-20 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app1',
            name='bustime',
        ),
    ]
