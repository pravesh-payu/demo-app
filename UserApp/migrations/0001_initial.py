# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2022-03-21 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('posts_count', models.IntegerField(default=0)),
            ],
        ),
    ]