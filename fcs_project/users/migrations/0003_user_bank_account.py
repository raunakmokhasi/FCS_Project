# Generated by Django 2.2.6 on 2019-10-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191029_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bank_account',
            field=models.FloatField(default=100000.0),
        ),
    ]