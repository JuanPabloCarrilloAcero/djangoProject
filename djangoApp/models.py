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
    students = models.ManyToManyField(Student, related_name="courses", blank=True)
    professors = models.ManyToManyField(Professor, related_name="courses", blank=True)

    def __str__(self):
        return f"{self.name}"


class Assignment(models.Model):
    name = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, related_name="assignments")

    def __str__(self):
        return f"{self.name}"

class Upload(models.Model):
    upload = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)
    students = models.ManyToManyField(Student, related_name="uploads")
    assignments = models.ManyToManyField(Assignment, related_name="uploads")
