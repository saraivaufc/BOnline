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
                ('is_administrator', models.BooleanField(default=False, verbose_name='administrator status')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('first_name', models.CharField(help_text='Please enter you first name.', max_length=100, null=True, verbose_name='First Name ')),
                ('last_name', models.CharField(help_text='Please enter you last name.', max_length=100, null=True, verbose_name='Last Name ')),
                ('email', models.EmailField(help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to=b'documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Phone', blank=True)),
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
                ('cep', models.CharField(help_text=b'Format: XXXXX-XXX', max_length=9, verbose_name='CEP')),
                ('street', models.CharField(help_text='Please enter street.', max_length=255, verbose_name='Street')),
                ('district', models.CharField(help_text='Please enter district.', max_length=255, verbose_name='District')),
                ('city', models.CharField(help_text='Please enter city.', max_length=255, verbose_name='City')),
                ('state', models.CharField(help_text='Please enter state.', max_length=255, verbose_name='State')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['cep'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Attendee',
                'verbose_name_plural': 'Attendees',
            },
            bases=('bo.person',),
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
