# Generated by Django 4.1 on 2022-09-27 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0003_product_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='favorites',
            new_name='favourites',
        ),
    ]