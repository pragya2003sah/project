# Generated by Django 4.2.5 on 2023-09-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_app1_bustime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app1',
            name='departure',
        ),
        migrations.AlterField(
            model_name='app1',
            name='bustroute',
            field=models.IntegerField(verbose_name='busroute'),
        ),
        migrations.AlterField(
            model_name='app1',
            name='distance',
            field=models.CharField(max_length=255, verbose_name='distance'),
        ),
        migrations.AlterField(
            model_name='app1',
            name='latitude',
            field=models.CharField(max_length=255, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='app1',
            name='longitude',
            field=models.CharField(max_length=255, verbose_name='longitude'),
        ),
    ]