# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('race_type', models.CharField(max_length=2, choices=[('RA', 'Stage Rally'), ('RX', 'RallyCross'), ('TX', 'Tarmac RallyCross'), ('EX', 'Enduro RallyCross'), ('AX', 'Autocross')])),
                ('location', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=25)),
                ('address2', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2, choices=[('CA', 'California'), ('NV', 'Nevada'), ('AZ', 'Arizona'), ('OR', 'Oregon')])),
                ('zip', models.IntegerField()),
                ('max_entries', models.CharField(max_length=3)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
