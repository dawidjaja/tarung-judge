# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0005_auto_20171012_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='attempt',
            name='status',
            field=models.IntegerField(choices=[(0, 'Wrong Answer'), (1, 'Accepted'), (2, 'Runtime Error'), (3, 'Server Error'), (4, 'Timed Out'), (5, 'Accepted (Testing)')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(20, 'Mudah'), (40, 'Sedang'), (70, 'Sulit')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='template',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='question',
            name='contest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Contest'),
        ),
    ]
