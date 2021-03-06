# Generated by Django 3.1.7 on 2021-03-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NationalID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=128)),
                ('number', models.CharField(max_length=14)),
                ('validity', models.BooleanField(default=False)),
                ('birth_year', models.IntegerField(default=0)),
                ('birth_month', models.IntegerField(default=0)),
                ('birth_day', models.IntegerField(default=0)),
            ],
        ),
    ]
