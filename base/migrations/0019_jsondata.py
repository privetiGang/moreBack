# Generated by Django 3.2.8 on 2021-10-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_favouritedatasets'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField()),
            ],
        ),
    ]
