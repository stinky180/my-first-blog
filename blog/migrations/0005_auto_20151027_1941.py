# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151027_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='races',
            name='address2',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
