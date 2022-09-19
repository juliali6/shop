from django.shortcuts import render, redirect
from django.views import View

from category_app.models import Product
from reviews_app.forms.reviews import ReviewForm


class AddReview(View):
    """View добавления отзывов"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect('/')
