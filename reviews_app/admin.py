from django.contrib import admin

from .models import Reviews


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'rating', 'content_object', 'image')
