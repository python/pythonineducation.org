# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]