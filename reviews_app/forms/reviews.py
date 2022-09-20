from django import forms

from reviews_app.models import Reviews, MediaReview


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class ImageForm(forms.ModelForm):
    class Meta:
        model = MediaReview
        fields = ('image_reviews',)
