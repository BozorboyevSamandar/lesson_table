from rest_framework import viewsets
from rest_framework.decorators import action
from .models import StudentGroup, Student, Teacher, Classroom, Lesson, LessonTable
from .serializers import StudentGroupSerializer, StudentSerializer, TeacherSerializer, ClassroomSerializer, \
    LessonSerializer, \
    LessonTableSerializer


# Create your views here.
class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonTableViewSet(viewsets.ModelViewSet):
    queryset = LessonTable.objects.all()
    serializer_class = LessonTableSerializer
