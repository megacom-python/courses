from django.urls import path
from main import views

urlpatterns = [
    path(
        "courses/", views.CourseCreateAPIView.as_view(), name="create-courses"
    )
]
