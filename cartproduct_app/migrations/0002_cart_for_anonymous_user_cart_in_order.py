# Generated by Django 4.1 on 2022-09-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartproduct_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
