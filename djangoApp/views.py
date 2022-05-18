import json

from django.shortcuts import render
from django.http import JsonResponse
from djangoApp.models import *
from djangoApp.serializers import *
from djangoApp.forms import *
from django.views.decorators.csrf import *


def student_list(request):
    all_students = Student.objects.all()
    serialized_data = StudentSerializer().convert_all(all_students)
    return JsonResponse(serialized_data, status=200)


@csrf_exempt
def student_new(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = StudentForm(data)
            if form.is_valid():
                student = form.save(commit=True)
                serialized_student = StudentSerializer().convert_one(student)
                return JsonResponse(serialized_student, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serialized_student = StudentSerializer().convert_one(student)
    return JsonResponse(serialized_student, status=200)


def student_edit(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = StudentForm(data)
            if form.is_valid():
                student = form.save(commit=True)
                serialized_student = StudentSerializer().convert_one(student)
                return JsonResponse(serialized_student, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def student_delete(request):
    pass


def course_list(request):
    all_courses = Course.objects.all()
    serialized_data = CourseSerializer().convert_all(all_courses)
    return JsonResponse(serialized_data, status=200)


@csrf_exempt
def course_new(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = CourseForm(data)
            if form.is_valid():
                course = form.save(commit=True)
                serialized_course = CourseSerializer().convert_one(course)
                return JsonResponse(serialized_course, status=200)
            else:
                raise Exception("not a valid format")
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    serialized_data = CourseSerializer().convert_one(course)
    return JsonResponse(serialized_data, status=200)


def course_edit(request):
    pass


def course_delete(request):
    pass


def professor_list(request):
    all_professors = Professor.objects.all()
    serialized_data = ProfessorSerializer().convert_all(all_professors)
    return JsonResponse(serialized_data, status=200)


@csrf_exempt
def professor_new(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = ProfessorForm(data)

            if form.is_valid():
                professor = form.save(commit=True)
                serialized_professor = ProfessorSerializer().convert_one(professor)
                return JsonResponse(serialized_professor, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def professor_detail(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    serialized_professor = ProfessorSerializer().convert_one(professor)
    return JsonResponse(serialized_professor, status=200)


def professor_edit(request):
    pass


def professor_delete(request):
    pass


def assignment_list(request):
    all_assignments = Assignment.objects.all()
    serialized_data = AssignmentSerializer().convert_all(all_assignments)
    return JsonResponse(serialized_data, status=200)


@csrf_exempt
def assignment_new(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = AssignmentForm(data)
            if form.is_valid():
                assignment = form.save(commit=True)
                serialized_assignment = AssignmentSerializer().convert_one(assignment)
                return JsonResponse(serialized_assignment, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def assignment_detail(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    serialized_assignment = AssignmentSerializer().convert_one(assignment)
    return JsonResponse(serialized_assignment, status=200)


def assignment_edit(request):
    pass


def assignment_delete(request):
    pass
