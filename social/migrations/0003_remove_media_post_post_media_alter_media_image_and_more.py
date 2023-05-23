# Generated by Django 4.2.1 on 2023-05-23 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_rename_image_or_video_media_image_media_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.ManyToManyField(blank=True, to='social.media'),
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]