from django.shortcuts import render, redirect
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Category
from profile_app.forms.update_profile import UpdateProfileForm, UpdateProForm


class UserUpdate(CartMixin, View):
    """Вью для редактирования профиля."""

    def get(self, request):
        user_form = UpdateProfileForm(instance=request.user)
        profile_form = UpdateProForm(instance=request.user.profile)
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'title': 'Editing profile',
            'user_form': user_form,
            'profile_form': profile_form,
            'categories': categories,
            'cart': self.cart
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
