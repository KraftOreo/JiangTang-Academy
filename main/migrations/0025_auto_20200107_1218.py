# Generated by Django 2.2.7 on 2020-01-07 12:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20200107_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 12, 18, 54, 419478, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 12, 18, 54, 416089, tzinfo=utc), verbose_name='date published'),
        ),
    ]
