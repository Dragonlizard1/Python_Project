# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='descrip',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='descrips', to='course.courses'),
        ),
    ]
