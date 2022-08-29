from django.db import models

from category_app.models import Product


class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display_type = models.CharField(max_length=255, verbose_name='Display type')
    processor_freq = models.CharField(max_length=255, verbose_name='Processor freq')
    ram = models.CharField(max_length=255, verbose_name='Ram')  # оперативная память
    video = models.CharField(max_length=255, verbose_name='Video card')
    time_without_charge = models.CharField(max_length=255, verbose_name='Battery life')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
