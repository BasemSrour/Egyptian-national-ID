# Generated by Django 3.1.7 on 2021-03-09 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egyNationalId', '0003_nationalid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nationalid',
            name='name',
        ),
    ]
