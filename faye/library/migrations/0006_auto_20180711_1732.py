# Generated by Django 2.0.6 on 2018-07-11 22:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20180711_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryobject',
            name='acq_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 11, 22, 32, 48, 308104, tzinfo=utc), verbose_name='date acquired'),
        ),
        migrations.AlterField(
            model_name='libraryobject',
            name='description',
            field=models.TextField(default='n/a', max_length=1000),
        ),
    ]
