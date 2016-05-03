# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_institution_monitorings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='monitorings',
            field=models.ManyToManyField(to='monitorings.Monitoring', verbose_name='Monitorings'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teryt.JST', verbose_name='Community'),
        ),
    ]