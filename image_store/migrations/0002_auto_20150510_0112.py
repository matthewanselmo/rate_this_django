# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
