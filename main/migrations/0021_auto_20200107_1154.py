# Generated by Django 2.2.7 on 2020-01-07 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200107_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 54, 50, 46711, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 54, 50, 44098, tzinfo=utc), verbose_name='date published'),
        ),
    ]
