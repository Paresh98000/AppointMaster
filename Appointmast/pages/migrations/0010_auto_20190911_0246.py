# Generated by Django 2.2.2 on 2019-09-10 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20190911_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='userid',
            new_name='clientid',
        ),
    ]
