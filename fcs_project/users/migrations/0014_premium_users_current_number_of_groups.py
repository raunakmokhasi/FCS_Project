# Generated by Django 2.2.6 on 2019-10-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_premium_users_number_of_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='premium_users',
            name='current_number_of_groups',
            field=models.IntegerField(default=0),
        ),
    ]
