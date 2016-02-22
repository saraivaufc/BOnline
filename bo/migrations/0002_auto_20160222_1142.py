# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendee',
            new_name='GeneralUser',
        ),
        migrations.AlterModelOptions(
            name='generaluser',
            options={'verbose_name': 'GeneralUser', 'verbose_name_plural': 'GeneralUsers'},
        ),
    ]
