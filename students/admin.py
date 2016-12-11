from django.contrib import admin
from students.models.students import Student
from students.models.groups import Group
from students.models.exams import Exam

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
