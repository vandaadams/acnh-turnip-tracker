# Generated by Django 3.0.7 on 2020-07-14 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0004_auto_20200714_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnip',
            old_name='resident',
            new_name='user',
        ),
    ]