# Generated by Django 2.0.6 on 2018-07-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20180712_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryobject',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
