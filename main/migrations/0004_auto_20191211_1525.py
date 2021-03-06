# Generated by Django 2.2.7 on 2019-12-11 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191211_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='tutorial_category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 15, 25, 53, 593339, tzinfo=utc), verbose_name='date published'),
        ),
    ]
