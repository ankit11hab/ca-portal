# Generated by Django 3.2.7 on 2021-09-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subIdea', '0003_alter_post_validate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='validate',
            field=models.BooleanField(default=0),
        ),
    ]
