# Generated by Django 3.2.12 on 2022-11-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='total',
            field=models.BigIntegerField(default=0, verbose_name='puntaje total'),
        ),
    ]
