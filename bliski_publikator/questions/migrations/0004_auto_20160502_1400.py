# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20160501_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Choice')),
            ],
            options={
                'verbose_name': 'Choice answer',
                'verbose_name_plural': 'Choice answers',
            },
        ),
        migrations.RemoveField(
            model_name='answerbool',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answerdate',
            name='answer',
        ),
        migrations.AlterField(
            model_name='answertext',
            name='answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer'),
        ),
        migrations.DeleteModel(
            name='AnswerBool',
        ),
        migrations.DeleteModel(
            name='AnswerDate',
        ),
    ]