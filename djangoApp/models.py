from django.db import models

class Student(models.Model):
    name = models.CharField()

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField()
    description = models.CharField()
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return f"{self.name}"