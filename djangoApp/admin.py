from django.contrib import admin
from djangoApp.models import *


class StudentAdmin(admin.ModelAdmin):
    model = Student
    readonly_fields = ["id"]
    list_display = ["id", "name", "courses"]


admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Upload)
