from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Customer(models.Model):

    user = models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)

    def __str__(self):
        return 'Customer: {} {}'.format(self.user.first_name, self.user.last_name)
