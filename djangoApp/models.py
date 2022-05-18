from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Professor(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    students = models.ManyToManyField(Student, related_name="courses")
    professors = models.ManyToManyField(Professor, related_name="professors")

    def __str__(self):
        return f"{self.name}"


class Assignment(models.Model):
    name = models.CharField(max_length=64)
    course = models.ManyToManyField(Course, related_name="courses")
    student = models.ManyToManyField(Student, related_name="student")

    def __str__(self):
        return f"{self.name}"
