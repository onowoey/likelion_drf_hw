# Generated by Django 4.2.20 on 2025-07-15 03:56

from django.db import migrations, models
import singer.models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0003_tag_singer_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=singer.models.image_upload_path),
        ),
    ]
