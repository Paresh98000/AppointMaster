# Generated by Django 2.2.2 on 2019-08-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('serviceid', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('providerid', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('time_start_h', models.CharField(max_length=2)),
                ('time_start_m', models.CharField(max_length=2)),
                ('time_end_h', models.CharField(max_length=2)),
                ('time_end_m', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('day', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('stype', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
