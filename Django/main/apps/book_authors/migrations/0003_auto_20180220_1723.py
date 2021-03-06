# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_authors_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_authors',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book_authors',
            name='book',
        ),
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='author', to='book_authors.books'),
        ),
        migrations.DeleteModel(
            name='book_authors',
        ),
    ]
