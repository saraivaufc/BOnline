# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0003_occurrence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='is_administrator',
        ),
    ]
