from django.urls import path, include

from reviews_app.api.views.router import api_router
from reviews_app.views.review import add_review

urlpatterns = [

    path('review/<str:ct_model>/<str:slug>/', add_review, name='add_review'),
    path('api/', include(api_router.urls)),

]
