from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return f"{self.name}"