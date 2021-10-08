# Generated by Django 3.1.2 on 2021-10-07 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='POCBulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('submit_date', models.DateField(default=django.utils.timezone.now)),
                ('csv_file', models.FileField(upload_to='image-uploads')),
                ('correct_poc', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pocbulk_submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='POC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('submit_date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=70)),
                ('design', models.CharField(max_length=60)),
                ('college', models.CharField(max_length=90)),
                ('contact', models.CharField(max_length=13)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poc_submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('submit_date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('submit_date', models.DateField(default=django.utils.timezone.now)),
                ('shared_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_submissions', to='dashboard.shareablepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'shared_post')},
            },
        ),
    ]
