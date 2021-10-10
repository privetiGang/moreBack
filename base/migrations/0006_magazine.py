# Generated by Django 3.2.8 on 2021-10-09 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_mts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField()),
                ('phone_number', models.TextField()),
                ('address', models.TextField()),
                ('metafields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.metafields')),
            ],
        ),
    ]
