# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151027_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='races',
            name='address2',
            field=models.CharField(max_length=5),
        ),
    ]
