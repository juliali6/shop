from django.contrib import auth
from django.shortcuts import redirect, render
from django.views import View

from customer_app.forms.authorization import AuthForm


class AuthView(View):
    """View for authorization."""

    @staticmethod
    def get(request):
        form = AuthForm()
        context = {
            'auth_form': form,
        }
        return render(request, 'authorization.html', context)

    @staticmethod
    def post(request):
        form = AuthForm(request.POST)
        error = False

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user is not None:
                auth.login(request, user)

                next_page = request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        context = {
            'auth_form': form,
            'error': error,
        }

        return render(request, 'authorization.html', context)