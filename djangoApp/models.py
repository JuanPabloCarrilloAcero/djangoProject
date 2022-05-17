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
    professors = models.ForeignKey(Professor, related_name="professors", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Assignment(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, related_name="courses", on_delete=models.DO_NOTHING)
    student = models.ManyToManyField(Student, related_name="student")

    def __str__(self):
        return f"{self.name}"
