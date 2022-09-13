from user_app.models import User
from django import forms

from profile_app.models import Profile


class UpdateProfileForm(forms.ModelForm):
    """Form for update profile."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UpdateProForm(forms.ModelForm):
    """Form for update profile."""

    class Meta:
        model = Profile
        fields = ['avatar', 'phone']