# Generated by Django 2.2.3 on 2019-07-20 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_auto_20190719_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homicide',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Other or Unknown')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='killergender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Other or Unknown')], default='U', max_length=1),
        ),
    ]
