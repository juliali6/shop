from django.db import models

from category_app.models import Product


class Smartphone(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display_type = models.CharField(max_length=255, verbose_name='Display type')
    resolution = models.CharField(max_length=255, verbose_name='Screen resolution')  # разрешение экрана
    accum_volume = models.CharField(max_length=255, verbose_name='Battery capacity')  # объем батареи
    ram = models.CharField(max_length=255, verbose_name='Ram')  # оперативная память
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Maximum built-in memory')  # максю встр. памяти
    main_cam_mp = models.CharField(max_length=255, verbose_name='Main camera')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Front camera')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
