from django.contrib import admin
from django.forms import ModelChoiceField

from category_app.models import Category
from .models import *


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Smartphone, SmartphoneAdmin)
