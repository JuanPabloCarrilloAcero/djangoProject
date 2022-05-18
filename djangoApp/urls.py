from django.urls import path
from djangoApp import views

urlpatterns = [
    path('students/', views.student_list, name="student_list"),
    path('students/new', views.student_new, name="student_new"),
    path('students/<int:student_id>', views.student_detail, name="student_detail"),
    path('students/<int:student_id>/edit', views.student_edit, name="student_edit"),
    path('students/<int:student_id>/delete', views.student_delete, name="student_delete"),
    path('students/upload', views.student_upload, name="student_upload"),

    path('courses/', views.course_list, name="course_list"),
    path('courses/new', views.course_new, name="course_new"),
    path('courses/<int:course_id>', views.course_detail, name="course_detail"),
    path('courses/<int:course_id>/edit', views.course_edit, name="course_edit"),
    path('courses/<int:course_id>/delete', views.course_delete, name="course_delete"),

    path('professors/', views.professor_list, name="professor_list"),
    path('professors/new', views.professor_new, name="professor_new"),
    path('professors/<int:professor_id>', views.professor_detail, name="professor_detail"),
    path('professors/<int:professor_id>/edit', views.professor_edit, name="professor_edit"),
    path('professors/<int:professor_id>/delete', views.professor_delete, name="professor_delete"),
    path('upload/<int:upload_id>/<int:student_id>/rate', views.professor_upload, name="professor_upload"),

    path('assignments/', views.assignment_list, name="assignment_list"),
    path('assignments/new', views.assignment_new, name="assignment_new"),
    path('assignments/<int:assignment_id>', views.assignment_detail, name="assignment_detail"),
    path('assignments/<int:assignment_id>/edit', views.assignment_edit, name="assignment_edit"),
    path('assignments/<int:assignment_id>/delete', views.assignment_delete, name="assignment_delete")
]
