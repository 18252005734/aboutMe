# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WebManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 13, 7, 1, 25, 644000, tzinfo=utc), verbose_name='\u53d1\u8868\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
    ]
