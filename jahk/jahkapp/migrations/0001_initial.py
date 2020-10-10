# Generated by Django 3.0.6 on 2020-10-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_content', models.TextField()),
                ('event_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
