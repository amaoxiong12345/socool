# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-10 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='goods_id',
            field=models.ForeignKey(db_column='goods_id', on_delete=django.db.models.deletion.CASCADE, to='index.Goods', verbose_name='商品'),
        ),
    ]