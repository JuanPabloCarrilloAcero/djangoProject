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


@csrf_exempt
def student_edit(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        if request.method == "POST":
            data = json.load(request)
            form = StudentForm(data, instance=student)
            if form.is_valid():
                student = form.save(commit=True)
                serialized_student = StudentSerializer().convert_one(student)
                return JsonResponse(serialized_student, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


@csrf_exempt
def student_delete(request, student_id):
    try:
        if request.method == "POST":
            Student.objects.get(id=student_id).delete()
            return JsonResponse({"message": "student deleted!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)})


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


@csrf_exempt
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    serialized_data = CourseSerializer().convert_one(course)
    return JsonResponse(serialized_data, status=200)

@csrf_exempt
def course_edit(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        if request.method == "POST":
            data = json.load(request)
            form = CourseForm(data, instance=course)
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


@csrf_exempt
def course_delete(request, course_id):
    try:
        if request.method == "POST":
            Course.objects.get(id=course_id).delete()
            return JsonResponse({"message": "course deleted!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)})


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

@csrf_exempt
def professor_edit(request, professor_id):
    try:
        professor = Professor.objects.get(id=professor_id)
        if request.method == "POST":
            data = json.load(request)
            form = ProfessorForm(data, instance=professor)
            if form.is_valid():
                professor = form.save(commit=True)
                serialized_professor = ProfessorSerializer().convert_one(professor)
                return JsonResponse(serialized_professor, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


@csrf_exempt
def professor_delete(request, professor_id):
    try:
        if request.method == "POST":
            Professor.objects.get(id=professor_id).delete()
            return JsonResponse({"message": "professor deleted!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)})


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
                raise Exception("form not valid")
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


def assignment_detail(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    serialized_assignment = AssignmentSerializer().convert_one(assignment)
    return JsonResponse(serialized_assignment, status=200)


@csrf_exempt
def assignment_edit(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        if request.method == "POST":
            data = json.load(request)
            form = AssignmentForm(data, instance=assignment)
            if form.is_valid():
                assignment = form.save(commit=True)
                serialized_assignment = AssignmentSerializer().convert_one(assignment)
                return JsonResponse(serialized_assignment, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


@csrf_exempt
def assignment_delete(request, assignment_id):
    try:
        if request.method == "POST":
            Assignment.objects.get(id=assignment_id).delete()
            return JsonResponse({"message": "assignment deleted!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)})

@csrf_exempt
def student_upload(request):
    try:
        if request.method == "POST":
            data = json.load(request)
            form = UploadForm(data)
            if form.is_valid():
                upload = form.save(commit=True)
                serialized_upload = UploadSerializer().convert_one(upload)
                return JsonResponse(serialized_upload, status=200)
            else:
                raise Exception("form not valid")
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)

@csrf_exempt
def professor_upload(request, upload_id, student_id):
    try:
        upload = Upload.objects.get(id=upload_id, students=student_id)
        if request.method == "POST":
            data = json.load(request)
            print(data)
            form = UploadForm(data, instance=upload)
            if form.is_valid():
                upload = form.save(commit=True)
                serialized_upload = UploadSerializer().convert_one(upload)
                return JsonResponse(serialized_upload, status=200)
        else:
            raise Exception("not a POST request")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)