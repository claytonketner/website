# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('is_index', models.BooleanField(default=False)),
                ('when_created', models.DateTimeField(help_text=b'If blank, current time will be used', null=True, blank=True)),
                ('views', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('published', models.BooleanField(default=True)),
                ('when_created', models.DateTimeField(help_text=b'If blank, current time will be used', null=True, blank=True)),
                ('when_modified', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(to='blog.Blog')),
            ],
            options={
                'ordering': ['when_created'],
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
            bases=(models.Model,),
        ),
    ]
