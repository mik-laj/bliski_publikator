# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 00:02
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_remove_question_max_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='count',
            field=jsonfield.fields.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
