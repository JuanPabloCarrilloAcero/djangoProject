from django.urls import path
from djangoApp import views

urlpatterns = [
    path('students/', views.student_list, name="student_list"),
    path('students/new', views.student_new, name="student_new"),
    path('students/<int:student_id>', views.student_detail, name="student_detail"),
    path('students/<int:student_id>/edit', views.student_edit, name="student_edit"),
    path('students/<int:student_id>/delete', views.student_delete, name="student_delete"),

    path('courses/', views.course_list, name="course_list"),
    path('courses/new', views.course_new, name="course_new"),
    path('courses/<int:course_id>', views.course_detail, name="course_detail"),
    path('courses/<int:course_id>/edit', views.course_edit, name="course_edit"),
    path('courses/<int:course_id>/delete', views.course_delete, name="course_delete")
]
