# Generated by Django 2.2.3 on 2019-07-19 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20190718_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homicide',
            old_name='method',
            new_name='means',
        ),
    ]
