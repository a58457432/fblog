# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-17 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fblog', '0004_fk_category'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fk_category',
            table='fk_category',
        ),
    ]
