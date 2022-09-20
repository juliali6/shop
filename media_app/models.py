from django.db import models

from user_app.models import User


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    file = models.ImageField(null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
