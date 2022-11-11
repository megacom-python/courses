from rest_framework import generics

from main.models import Course
from main.serializers import CourseSerializer


class CourseCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
