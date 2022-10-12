from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutUser(View):
    """Представление для выхода из аккаунта"""

    def get(self, request):
        logout(request)
        return redirect("/")
