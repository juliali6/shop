# from django.shortcuts import render
# from category_app.models import Product
#
#
# def product(request, product_id):
#     """Метод представления последних просмотренных товаров.
#     Макс. к-л 5 товаров."""
#
#     product = Product.objects.get(pk=product_id)
#     recently_viewed_products = None
#
#     if 'recently_viewed' in request.session:
#         if product_id in request.session['recently_viewed']:
#             request.session['recently_viewed'].remove(product_id)
#
#         products = Product.objects.filter(pk__in=request.session['recently_viewed'])
#         recently_viewed_products = sorted(products,
#                                           key=lambda x:request.session['recently_viewed'].index(x.id))
#         request.session['recently_viewed'].insert(0, product_id)
#         if len(request.session['recently_viewed']) > 5:
#             request.session['recently_viewed'].pop()
#     else:
#         request.session['recently_viewed'] = [product_id]
#
#     request.session.modified = True
#
#     context = {'product': product, 'c': recently_viewed_products}
#     return render(request, 'product_detail.html', context)
