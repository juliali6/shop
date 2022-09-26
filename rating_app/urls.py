from django.urls import path

from rating_app.views.rating import AddStarRating

urlpatterns = [
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),

]
