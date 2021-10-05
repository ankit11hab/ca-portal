# Generated by Django 3.2.8 on 2021-10-05 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import users.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('alcherid', models.CharField(blank=True, default=users.utils.create_new_ref_number, max_length=9, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(default='user', max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('graduation_year', models.CharField(max_length=200)),
                ('college_state', models.CharField(max_length=200)),
                ('college_city', models.CharField(max_length=200)),
                ('college_name', models.CharField(max_length=200)),
                ('position_of_responsibility', models.CharField(blank=True, max_length=200)),
                ('interested_modules', models.CharField(blank=True, max_length=200)),
                ('referred_by', models.CharField(blank=True, max_length=9)),
                ('referrals', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('provider', models.CharField(default='email', max_length=200)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('college_state', models.CharField(max_length=200)),
                ('college_city', models.CharField(max_length=200)),
                ('college_name', models.CharField(max_length=200)),
                ('referred_by', models.CharField(blank=True, max_length=9)),
                ('executive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executive', to=settings.AUTH_USER_MODEL)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
