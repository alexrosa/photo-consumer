# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-16 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='url_photo',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
