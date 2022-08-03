from django.urls import path, include
from rest_framework import routers
from .views import StudentGroupViewSet, StudentViewSet, TeacherViewSet, LessonViewSet, ClassroomViewSet, \
    LessonTableViewSet

router = routers.DefaultRouter()
router.register('student_group', StudentGroupViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('lessons', LessonViewSet)
router.register('lesson_table', LessonTableViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
