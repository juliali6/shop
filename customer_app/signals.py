from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from customer_app.models import Customer


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, *args, **kwargs):
    """Function signals for creating profile."""
    if not created:
        return

    profile = Customer(user=instance)
    profile.save()
