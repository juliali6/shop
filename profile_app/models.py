from user_app.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    """Модель профиля пользователя."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        max_length=17,
        blank=True,
        null=True
    )
    about = models.TextField(max_length=4096, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Покупатель: {self.user.username}'
