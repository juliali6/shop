from django.shortcuts import render, redirect
from django.views import View
from profile_app.forms.update_profile import UpdateProfileForm, UpdateProForm


class UserUpdate(View):
    """View for update profile."""

    @staticmethod
    def get(request):
        user_form = UpdateProfileForm(instance=request.user)
        profile_form = UpdateProForm(instance=request.user.profile)
        context = {
            'title': 'Editing profile',
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'update_profile.html', context)

    @staticmethod
    def post(request):
        user_form = UpdateProfileForm(instance=request.user, data=request.POST)
        profile_form = UpdateProForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile')
