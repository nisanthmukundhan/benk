# Generated by Django 4.1 on 2022-08-19 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_alter_register_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='slug',
        ),
    ]
