# from django.shortcuts import redirect
# from django.views import View
#
# from category_app.forms.review import ReviewForm
# from category_app.models import Product
#
#
# class AddReview(View):
#     """Класс представления для отзывов пользователей."""
#
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.product_id = pk
#             form.save()
#         return redirect('/')


