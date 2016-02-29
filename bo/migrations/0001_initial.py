# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bo.models.access
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('location', models.CharField(max_length=75, null=True, verbose_name='location', blank=True)),
                ('last_seen', models.DateTimeField(auto_now=True, verbose_name='last seen')),
                ('last_ip', models.GenericIPAddressField(null=True, verbose_name='last ip', blank=True)),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('first_name', models.CharField(help_text='Please enter you first name.', max_length=100, null=True, verbose_name='First Name ')),
                ('last_name', models.CharField(help_text='Please enter you last name.', max_length=100, null=True, verbose_name='Last Name ')),
                ('email', models.EmailField(help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to=b'documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('exists', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_joined'],
                'abstract': False,
                'verbose_name_plural': 'Persons',
                'db_table': 'auth_user',
                'verbose_name': 'Person',
                'swappable': 'AUTH_USER_MODEL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(help_text=b'Format: XXXXX-XXX', max_length=9, verbose_name='Zip Code')),
                ('street', models.CharField(help_text='Please enter street.', max_length=255, verbose_name='Street')),
                ('district', models.CharField(help_text='Please enter district.', max_length=255, verbose_name='District')),
                ('city', models.CharField(help_text='Please enter city.', max_length=255, verbose_name='City')),
                ('state', models.CharField(help_text='Please enter state.', max_length=255, verbose_name='State')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['zip_code'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'General User',
                'verbose_name_plural': 'General Users',
            },
            bases=('bo.person',),
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='enter the name of the event. Example: theft, damage, etc.', unique=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing.', verbose_name='Description')),
                ('image', models.ImageField(help_text='Please enter image to occurrence.', upload_to=b'documents/image/occurrence/%Y/%m/%d', verbose_name='Imagem')),
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
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizes',
            },
            bases=('bo.person',),
        ),
        migrations.CreateModel(
            name='OrganizerKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=bo.models.access.generate_key, max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('Person', models.ForeignKey(related_name='Organizer', blank=True, to='bo.Organizer', null=True)),
                ('creator', models.ForeignKey(verbose_name='Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['Person'],
                'verbose_name': 'Organizer Key',
                'verbose_name_plural': 'Organizes Key',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('observation', models.CharField(help_text='enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing.', max_length=255, null=True, verbose_name='Observation', blank=True)),
                ('image', models.ImageField(help_text='Enter image to report.', upload_to=b'documents/image/report/%Y/%m/%d', null=True, verbose_name='Imagem', blank=True)),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('address', models.ForeignKey(related_name='Address', verbose_name='Address', to='bo.Address')),
                ('occurrence', models.ForeignKey(related_name='Occurrence', verbose_name='Occurrence', to='bo.Occurrence')),
                ('person', models.ForeignKey(related_name='Person', verbose_name='Person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-occurrence'],
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(verbose_name='Address', blank=True, to='bo.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
