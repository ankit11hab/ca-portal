# Generated by Django 3.2.9 on 2022-09-03 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=200)),
                ('device', models.CharField(blank=True, max_length=100)),
                ('browser', models.CharField(blank=True, max_length=100)),
                ('browser_version', models.CharField(blank=True, max_length=100)),
                ('browser_family', models.CharField(blank=True, max_length=100)),
                ('os_name', models.CharField(blank=True, max_length=100)),
                ('os_version', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='image-uploads/')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ShareablePost',
            fields=[
                ('id', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('link_instagram', models.CharField(blank=True, max_length=500, null=True)),
                ('link_facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('is_instagram', models.BooleanField(default=False)),
                ('is_facebook', models.BooleanField(default=False)),
                ('media_id', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='image-uploads/')),
                ('caption', models.CharField(max_length=160)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likedusers', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.TextField(blank=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.shareablepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('Success', 'Success'), ('Warning', 'Warning'), ('Info', 'Info')], max_length=200)),
                ('isread', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
