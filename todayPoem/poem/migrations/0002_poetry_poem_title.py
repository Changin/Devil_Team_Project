# Generated by Django 2.0.5 on 2018-05-18 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poetry',
            name='poem_title',
            field=models.CharField(default='TITLE', max_length=30),
        ),
    ]
