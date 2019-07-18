# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-18 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_article_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
