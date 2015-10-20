# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('answered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, related_name='sent_questions', blank=True, to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(null=True, related_name='get_questions', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(null=True, blank=True, to='website.Question'),
        ),
    ]
