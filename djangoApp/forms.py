from django.forms import ModelForm
from djangoApp.models import *


class StudentForm(ModelForm):
    model = Student
    fields = ["name"]


class CourseForm(ModelForm):
    model = Course
    fields = ["name", "description"]
