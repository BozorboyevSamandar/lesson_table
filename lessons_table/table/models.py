from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class StudentGroup(models.Model):
    group_name = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )

    class Meta:
        ordering = ('group_name',)

    def __str__(self):
        return f"{self.group_name}-group"


class Student(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True)
    phone_no = models.CharField(max_length=13)
    group_id = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f"{self.first_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True)
    phone_no = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.username}"


class Classroom(models.Model):
    classroom_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )

    class Meta:
        ordering = ('classroom_number',)

    def __str__(self):
        return f"{self.classroom_number} - room"


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=150)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.lesson_name}"


class LessonTable(models.Model):
    day = [
        ('monday', 'monday',),
        ('tuesday', 'tuesday',),
        ('wednesday', 'wednesday',),
        ('thursday', 'thursday',),
        ('friday', 'friday',),
        ('saturday', 'saturday',),
    ]
    day = models.CharField(max_length=150, choices=day)
    lesson_name = models.ManyToManyField(Lesson)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    group_id = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.lesson_name}"
