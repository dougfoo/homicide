# Generated by Django 2.2.2 on 2019-07-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0018_auto_20190720_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homicide',
            name='ethnicity',
            field=models.CharField(choices=[('A', 'Asian'), ('W', 'White'), ('B', 'Black'), ('H', 'Hispanic'), ('O', 'Other'), ('O', 'Unknown')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other or Unknown')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='killerethnicity',
            field=models.CharField(choices=[('A', 'Asian'), ('W', 'White'), ('B', 'Black'), ('H', 'Hispanic'), ('O', 'Other'), ('O', 'Unknown')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='killergender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other or Unknown')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='motive',
            field=models.CharField(choices=[('D', 'Dispute'), ('G', 'Gang'), ('F', 'Family/Domestic'), ('R', 'Robbery'), ('O', 'Other or Unknown')], default='O', max_length=1),
        ),
    ]
