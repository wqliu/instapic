# Generated by Django 2.2.7 on 2020-02-16 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_auto_20191209_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_avatar',
        ),
    ]
