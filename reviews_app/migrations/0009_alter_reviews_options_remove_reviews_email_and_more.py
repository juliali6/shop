# Generated by Django 4.1 on 2022-10-26 09:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('reviews_app', '0008_remove_reviews_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='text',
        ),
        migrations.AddField(
            model_name='reviews',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.FloatField(default=1, help_text='1-5', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='reviews',
            name='review',
            field=models.TextField(default=None, max_length=256, verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/%Y', verbose_name='Картинка отзыва'),
        ),
        migrations.DeleteModel(
            name='MediaReview',
        ),
    ]
