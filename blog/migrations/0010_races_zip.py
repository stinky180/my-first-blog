# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20151028_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='races',
            name='zip',
            field=localflavor.us.models.USZipCodeField(null=True, max_length=10),
        ),
    ]
