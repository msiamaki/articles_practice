# Generated by Django 4.2 on 2024-04-04 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article_app', '0002_comment_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_comment',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_name_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name="Comment's author"),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
