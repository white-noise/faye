# Generated by Django 2.0.6 on 2018-07-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20180712_1450'),
        ('produce', '0005_visualobject_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualobject',
            name='cited_works',
            field=models.ManyToManyField(blank=True, to='library.LibraryObject'),
        ),
        migrations.AddField(
            model_name='writtenobject',
            name='cited_works',
            field=models.ManyToManyField(blank=True, to='library.LibraryObject'),
        ),
    ]
