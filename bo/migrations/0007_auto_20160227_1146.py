# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0006_auto_20160227_0937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralUser',
            new_name='General',
        ),
    ]
