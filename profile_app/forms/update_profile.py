from user_app.models import User
from django import forms

from profile_app.models import Profile


class UpdateProfileForm(forms.ModelForm):
    """Форма редактирования профиля:
    'имя','фамилия' и 'электронная почта'."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UpdateProForm(forms.ModelForm):
    """Форма редактирования профиля:
    'аватар', 'номер телефона'."""

    class Meta:
        model = Profile
        fields = ['avatar', 'phone']
