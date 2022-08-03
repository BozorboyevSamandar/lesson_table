from django.contrib import admin
from .models import StudentGroup, Classroom, Student, Teacher, Lesson, LessonTable


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group_id')


admin.site.register(Student, StudentAdmin),


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


admin.site.register(Teacher, TeacherAdmin),


class LessonTableAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'teacher_id',
        'classroom',
        'group_id',
    )


admin.site.register(LessonTable, LessonTableAdmin),

admin.site.register(StudentGroup),
admin.site.register(Classroom),
admin.site.register(Lesson),
