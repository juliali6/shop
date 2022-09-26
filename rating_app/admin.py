from django.contrib import admin

from rating_app.models import Rating, RatingStar


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "product", "ip")


admin.site.register(RatingStar)
