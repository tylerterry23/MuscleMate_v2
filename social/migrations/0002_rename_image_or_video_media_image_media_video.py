# Generated by Django 4.2.1 on 2023-05-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='image_or_video',
            new_name='image',
        ),
        migrations.AddField(
            model_name='media',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_videos/'),
        ),
    ]
