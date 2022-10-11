from django import forms

from reviews_app.models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text",)


class ReviewImageForm(ReviewForm):

    image = forms.ImageField(required=False)

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ('image',)
