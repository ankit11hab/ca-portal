# Generated by Django 3.2.9 on 2022-08-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='alcherid',
            field=models.CharField(blank=True, default='ALC-1661037072.5461414', max_length=100, unique=True),
        ),
    ]
