# Generated by Django 2.2.7 on 2020-01-07 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200107_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 27, 39, 802915, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 27, 39, 799500, tzinfo=utc), verbose_name='date published'),
        ),
    ]
