from django.shortcuts import render, redirect
from django.views import View

from category_app.models import Product
from reviews_app.forms.reviews import ReviewForm, ImageForm


class AddReview(View):
    """View добавления отзывов"""

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


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'product_detail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'product_detail.html', {'form': form})
