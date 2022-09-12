from django.shortcuts import redirect, render
from django.views import View

from customer_app.forms.registration import RegistrationForm


class RegistrationView(View):
    """View for registration."""

    @staticmethod
    def get(request):
        form = RegistrationForm()
        context = {
            'reg_form': form,
        }
        return render(request, 'registration.html', context)

    @staticmethod
    def post(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'reg_form': form,
        }
        return render(request, 'registration.html', context)
