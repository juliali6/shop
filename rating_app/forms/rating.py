from django import forms

from rating_app.models import RatingStar, Rating


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)

