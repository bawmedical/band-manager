# Generated by Django 4.0.6 on 2022-07-20 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0004_rename_color_tag_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 20, 19, 46, 48, 368519)),
            preserve_default=False,
        ),
    ]
