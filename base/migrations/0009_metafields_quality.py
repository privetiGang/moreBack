# Generated by Django 3.2.8 on 2021-10-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211009_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='metafields',
            name='quality',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
