# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20171205_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
