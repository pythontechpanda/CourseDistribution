# Generated by Django 4.1.4 on 2023-01-14 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0008_alter_createpost_date_alter_followerscount_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 14, 12, 5, 57, 618555)),
        ),
    ]
