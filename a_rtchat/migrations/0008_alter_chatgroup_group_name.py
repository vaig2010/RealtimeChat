# Generated by Django 5.1 on 2024-09-01 11:16

import a_rtchat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0007_alter_chatgroup_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=a_rtchat.models.generate_group_name, max_length=128, unique=True),
        ),
    ]
