from django.urls import path

from reviews_app.review.review import AddReview

urlpatterns = [
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    # path("review/", ReviewImageAdd.as_view(), name="add_image_review"),

]
