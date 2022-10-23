from django.urls import path, include

from reviews_app.api.views.router import api_router
from reviews_app.review.review import AddReview

urlpatterns = [
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    # path("review/", ReviewImageAdd.as_view(), name="add_image_review"),
    path('api/', include(api_router.urls)),

]
