# Generated by Django 2.0.7 on 2018-08-08 00:47

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('manualtest', '0004_auto_20180808_0040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestCase',
            new_name='ProductTestCase',
        ),
    ]
