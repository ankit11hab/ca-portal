# Generated by Django 3.2.9 on 2022-09-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_alcherid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='alcherid',
            field=models.TextField(blank=True, default='create_new_ref_number', unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='referred_by',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='referred_by',
            field=models.TextField(blank=True),
        ),
    ]
