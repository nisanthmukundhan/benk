# Generated by Django 4.1 on 2022-08-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_remove_branch_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='slug',
        ),
    ]
