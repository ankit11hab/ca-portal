# Generated by Django 3.1.2 on 2021-10-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='instahandle',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
