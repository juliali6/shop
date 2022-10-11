from django.urls import path

from .views import AddReview

urlpatterns = [
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    # path("review/", ReviewImageAdd.as_view(), name="add_image_review"),

]
