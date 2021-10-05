# Generated by Django 3.2.8 on 2021-10-05 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_submissions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='media',
            name='shared_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_submissions', to='dashboard.shareablepost'),
        ),
    ]
