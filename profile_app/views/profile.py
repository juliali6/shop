from django.shortcuts import render, redirect
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Category
from profile_app.models import Profile


class ProfileUserView(CartMixin, View):
    """Представление отображения профиля."""

    def get(self, request):
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            categories = Category.objects.get_categories_for_left_sidebar()
            contex = {
                'title': 'Profile',
                'avatar': user,
                'categories': categories,
                'cart': self.cart
            }
            return render(request, "profile.html", contex)
        return redirect("login")



