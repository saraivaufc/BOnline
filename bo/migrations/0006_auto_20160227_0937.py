# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0005_auto_20160222_2348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generaluser',
            options={'verbose_name': 'General User', 'verbose_name_plural': 'General Users'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
    ]
