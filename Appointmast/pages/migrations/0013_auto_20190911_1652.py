# Generated by Django 2.2.2 on 2019-09-11 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20190911_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='providerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.sp'),
        ),
    ]
