from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.permissions import IsModerator, IsOwner
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.owner = self.request.user
        new_course.save()

