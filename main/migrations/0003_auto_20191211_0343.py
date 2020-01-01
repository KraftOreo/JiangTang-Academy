# Generated by Django 2.2.7 on 2019-12-11 03:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191210_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 3, 43, 54, 102832, tzinfo=utc), verbose_name='date published'),
        ),
    ]
