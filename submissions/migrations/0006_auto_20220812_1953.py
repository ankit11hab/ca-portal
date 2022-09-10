# Generated by Django 3.2.9 on 2022-08-12 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0005_auto_20220812_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='user',
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_submission', to='submissions.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.question')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.submission')),
            ],
        ),
    ]