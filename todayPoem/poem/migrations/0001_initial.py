# Generated by Django 2.0.5 on 2018-05-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem_text', models.CharField(max_length=500)),
                ('poem_writer', models.CharField(max_length=10)),
            ],
        ),
    ]