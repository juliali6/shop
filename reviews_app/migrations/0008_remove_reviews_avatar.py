# Generated by Django 4.1 on 2022-10-04 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0007_reviews_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='avatar',
        ),
    ]
