# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 05:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]