from django.shortcuts import render, redirect
from django.views import View
from profile_app.models import Profile


class ProfileUserView(View):
    """View for profile user."""

    def get(self, request):
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            contex = {
                'title': 'Profile',
                'avatar': user,
            }
            return render(request, "profile.html", contex)
        return redirect("login")


