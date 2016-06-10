# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'blog_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('memo', models.CharField(max_length=200)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'blog_comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category_rel', models.ManyToManyField(to='posts.Category')),
            ],
            options={
                'db_table': 'blog_post',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]