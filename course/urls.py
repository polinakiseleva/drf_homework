from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig

from course.views.course import CourseViewSet
from course.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from course.views.payments import PaymentsListAPIView, PaymentsCreateAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    # payments
    path('payment/create/', PaymentsCreateAPIView.as_view(), name='payment-create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
] + router.urls
