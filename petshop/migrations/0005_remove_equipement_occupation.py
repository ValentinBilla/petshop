# Generated by Django 3.2.16 on 2022-11-21 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0004_auto_20221121_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipement',
            name='occupation',
        ),
    ]
