# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rentalstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='completed',
        ),
        migrations.AddField(
            model_name='book',
            name='checked_in',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
