# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_races'),
    ]

    operations = [
        migrations.AddField(
            model_name='races',
            name='race_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
