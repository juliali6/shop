from django.shortcuts import render, redirect
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Product, Category
from reviews_app.forms.reviews import ReviewForm, ReviewImageForm
from reviews_app.models import Reviews, MediaReview


class AddReview(View):
    """Класс вью добавления отзывов"""

    def post(self, request, pk):

        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect('/')


# class ReviewImageAdd(CartMixin, View):
#     """Представление добавления картинок к отзывам"""
#
#     def get(self, request):
#         form = ReviewImageForm()
#         categories = Category.objects.get_categories_for_left_sidebar()
#
#         context = {
#             'title': 'Add a new review',
#             'form': form,
#             'categories': categories,
#             'cart': self.cart
#         }
#
#         return render(request, 'review.html', context)
#
#     @staticmethod
#     def post(request):
#         form_image = ReviewImageForm(request.POST, request.FILES)
#         files = request.FILES.getlist('image')
#
#         if len(files) > 5:
#             return render(request, 'product_detail.html', context={
#                 'title': 'Add review',
#                 'form': form_image,
#                 'error': 'Maximum 5 files!'
#             })
#
#         if form_image.is_valid():
#             review_object = form_image.save(commit=False)
#             review_object.user = request.user
#             review_object.save()
#             for f in files:
#                 MediaReview.objects.create(review=review_object, image=f)
#             return redirect('/')
#
#         context = {
#             'create_review': form_image,
#         }
#
#         return render(request, 'product_detail.html', context)

