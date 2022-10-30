from django import forms

from reviews_app.models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ['subject', 'review', 'rating']


class ImageReviewForm(ReviewForm):
    """Класс формы добавление изображение к отзыву"""

    image = forms.ImageField(
        label='Выберите фотографии(Не более 5)',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['image', ]
