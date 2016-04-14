# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('monitorings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoring',
            name='institutions',
            field=models.ManyToManyField(help_text='Specifies which institutions are covered by monitoring', to='institutions.Institution', verbose_name='Institution'),
        ),
        migrations.AddField(
            model_name='monitoring',
            name='logo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=b'', verbose_name='Logo'),
        ),
    ]