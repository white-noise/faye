# Generated by Django 2.0.6 on 2018-07-12 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20180711_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryobject',
            name='acq_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date acquired'),
        ),
    ]
