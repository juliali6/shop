from django import forms

from user_app.models import User


class LoginForm(forms.ModelForm):
    """Форма авторизации пользователей"""

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        """Метод проверки совпадения логина и пароля"""

        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['password'].label = 'Password'

    def clean(self):
        """Метод проверки корректных данных логина и пароля пользователя"""

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Login user "{username} not found in the system')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Invalid password")
        return self.cleaned_data
