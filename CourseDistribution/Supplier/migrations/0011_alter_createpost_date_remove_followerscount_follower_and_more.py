# Generated by Django 4.1.4 on 2023-01-14 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0010_alter_createpost_date_alter_followerscount_follower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 14, 12, 37, 50, 421268)),
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='follower',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='follower',
            field=models.CharField(default='12:37', max_length=1000),
            preserve_default=False,
        ),
    ]
