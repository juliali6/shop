# Generated by Django 4.1 on 2022-09-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0005_mediareview_delete_imagereview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='file',
        ),
        migrations.AddField(
            model_name='reviews',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='MediaReview'),
        ),
    ]
