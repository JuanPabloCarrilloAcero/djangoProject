from django.shortcuts import render
from django.http import JsonResponse
from djangoApp.models import *
from djangoApp.serializers import *

def student_list(request):
    all_students = Student.objects.all()
    serialized_data = StudentSerializer().convert_all(all_students)
    return JsonResponse(serialized_data, status=200)

def student_new(request):
    pass

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serialized_student = StudentSerializer().convert_one(student)
    return JsonResponse(serialized_student, status=200)

def student_edit(request):
    pass

def student_delete(request):
    pass

def course_list(request):
    all_courses = Course.objects.all()
    serialized_data = CourseSerializer().convert_all(all_courses)
    return JsonResponse(serialized_data, status=200)

def course_new(request):
    pass

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    serialized_data = CourseSerializer().convert_one(course)
    return JsonResponse(serialized_data, status=200)

def course_edit(request):
    pass

def course_delete(request):
    pass