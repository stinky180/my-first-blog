# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_races_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='races',
            name='event_details',
            field=models.TextField(null=True),
        ),
    ]
