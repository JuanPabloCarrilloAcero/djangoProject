from django import forms
from djangoApp.models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
