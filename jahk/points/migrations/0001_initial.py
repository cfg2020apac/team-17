# Generated by Django 3.1.2 on 2020-10-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('point', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]