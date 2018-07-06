# Generated by Django 2.0.6 on 2018-07-06 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryobject',
            name='acq_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 6, 20, 24, 33, 417567, tzinfo=utc), verbose_name='date acquired'),
        ),
    ]
