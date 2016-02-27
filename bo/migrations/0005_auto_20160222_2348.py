# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0004_remove_person_is_administrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='image',
            field=models.ImageField(default=1, help_text='Please enter image to occurrence.', verbose_name='Imagem', upload_to=b'documents/image/occurrence/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
