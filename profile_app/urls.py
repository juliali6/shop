from django.contrib.auth.decorators import login_required
from django.urls import path, include

from profile_app.api.views.router import api_router
from profile_app.views.authorization import LoginView
from profile_app.views.logout import LogoutUser
from profile_app.views.profile import ProfileUserView
from profile_app.views.registration import RegistrationView
from profile_app.views.update_profile import UserUpdate

urlpatterns = [
    path('registration', RegistrationView.as_view(), name='registration'),
    path('profile/update', login_required(UserUpdate.as_view()), name='update_profile'),
    path('logout', LogoutUser.as_view(), name='logout_page'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', login_required(ProfileUserView.as_view()), name='profile_page'),
    path('api/', include(api_router.urls)),
]
