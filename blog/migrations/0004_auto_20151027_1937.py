# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_races_race_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='races',
            old_name='location',
            new_name='event_name',
        ),
    ]
