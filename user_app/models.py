from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    # phone = models.CharField(
    #     validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
    #     max_length=17,
    #     unique=True,
    # )
    #
    # about_description = models.TextField(max_length=500, blank=True)
    # is_email_verified = models.BooleanField(default=False)

