# Generated by Django 2.2.3 on 2019-07-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_auto_20190721_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('num', models.IntegerField()),
                ('ref', models.CharField(max_length=256)),
            ],
        ),
    ]