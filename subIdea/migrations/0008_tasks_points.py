# Generated by Django 3.2.7 on 2021-09-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subIdea', '0007_alter_tasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
