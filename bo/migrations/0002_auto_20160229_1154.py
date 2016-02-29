# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='datetime',
            field=models.DateTimeField(verbose_name='Datetime'),
            preserve_default=True,
        ),
    ]
