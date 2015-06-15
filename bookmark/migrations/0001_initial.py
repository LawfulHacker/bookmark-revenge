# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
                ('title', models.CharField(max_length=200)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=100))),
            ],
        ),
    ]
