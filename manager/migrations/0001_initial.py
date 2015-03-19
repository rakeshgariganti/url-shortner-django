# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longurl', models.URLField()),
                ('short', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
