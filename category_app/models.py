from django.contrib.contenttypes.models import ContentType
from django.db import models


class LatestProductManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to',)
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startwith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Name of category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=255, verbose_name='Title', default=True)
    slug = models.SlugField(unique=True, default=True)
    image = models.ImageField(verbose_name='Image', default=True)
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price', default=True)  # decimal_places к-л цифр после запятой

    def __str__(self):
        return self.title



