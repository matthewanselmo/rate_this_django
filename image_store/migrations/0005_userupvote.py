# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_store', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUpvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('_post', models.ForeignKey(to='image_store.Post')),
                ('_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
