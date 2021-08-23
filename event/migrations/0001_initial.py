# Generated by Django 3.2.4 on 2021-08-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=16)),
                ('day_of_event', models.DateField()),
                ('event_venue', models.CharField(max_length=16)),
                ('event_description', models.FileField(upload_to='')),
                ('event_duration', models.DateField()),
                ('event_link', models.CharField(max_length=30)),
                ('attendees', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]