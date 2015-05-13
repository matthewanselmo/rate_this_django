# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_store', '0005_userupvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='_user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='_user',
        ),
    ]
