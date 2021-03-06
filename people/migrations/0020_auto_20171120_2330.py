# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0019_auto_20170813_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='people.Event'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='people.Event'),
        ),
    ]
