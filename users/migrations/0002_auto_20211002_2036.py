# Generated by Django 3.1.2 on 2021-10-02 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='referred_by_user',
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='referred_by_user',
        ),
    ]