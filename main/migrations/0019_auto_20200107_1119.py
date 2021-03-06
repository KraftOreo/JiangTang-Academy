# Generated by Django 2.2.7 on 2020-01-07 11:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200107_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tutorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Tutorial', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 19, 11, 431692, tzinfo=utc), verbose_name='date published'),
        ),
    ]
