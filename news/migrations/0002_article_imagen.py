# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-29 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='news/'),
        ),
    ]
