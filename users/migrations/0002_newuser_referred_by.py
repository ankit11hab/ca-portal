# Generated by Django 3.1.2 on 2021-10-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='referred_by',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
