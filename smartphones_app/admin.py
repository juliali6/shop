from PIL import Image
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, ModelForm
from django.utils.safestring import mark_safe

from category_app.models import Category
from .models import *


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red;">Uploading an image with a minimum resolution {}x{}</span>'.format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Maximum image size 10MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Image is smaller than minimum resolution!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Image is bigger than maximum resolution!')
        return image


class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'

    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Smartphone, SmartphoneAdmin)
