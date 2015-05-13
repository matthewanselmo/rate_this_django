# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_store', '0006_auto_20150513_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userupvote',
            old_name='_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='userupvote',
            old_name='_user',
            new_name='user',
        ),
    ]
