# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bo', '0002_auto_20160222_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='enter the name of the event. Example: theft, damage, etc.', unique=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing.', verbose_name='Description')),
                ('image', models.ImageField(default=None, upload_to=b'documents/image/occurrence/%Y/%m/%d', blank=True, help_text='Please enter image to occurrence.', null=True, verbose_name='Imagem')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Occurrence',
                'verbose_name_plural': 'Occurrences',
            },
            bases=(models.Model,),
        ),
    ]
