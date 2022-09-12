from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    """Form for registration."""

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user
