# Generated by Django 3.2.8 on 2021-10-09 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20211009_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metafields',
            old_name='date_finish',
            new_name='dates_finish',
        ),
    ]
