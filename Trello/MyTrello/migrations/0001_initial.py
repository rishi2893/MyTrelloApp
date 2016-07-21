# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160715074857 on 2016-07-21 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField(verbose_name='Date Published:')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=150)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyTrello.Board')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=500)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyTrello.Card')),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
