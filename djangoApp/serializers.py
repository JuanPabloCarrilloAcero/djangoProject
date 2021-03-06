from builtins import object
from djangoApp.models import *


class StudentSerializer(object):
    @staticmethod
    def convert_all(self):
        serialized_students = {"students": []}

        for _ in self:
            serialized_student = StudentSerializer.convert_one(_)
            serialized_students["students"].append(serialized_student)

        return serialized_students

    @staticmethod
    def convert_one(self):

        serialized_students = {
            "id": self.id,
            "name": self.name,
        }
        return serialized_students


class CourseSerializer(object):

    @staticmethod
    def convert_all(self):
        serialized_courses = {"courses": []}

        for _ in self:
            serialized_course = CourseSerializer.convert_one(_)
            serialized_courses["courses"].append(serialized_course)

        return serialized_courses

    @staticmethod
    def convert_one(self):
        serialized_courses = {"id": self.id, "name": self.name, "description": self.description,
                              "professor": ProfessorSerializer.convert_all(self.professors.all()),
                              "students": StudentSerializer.convert_all(self.students.all())}
        return serialized_courses


class ProfessorSerializer(object):

    @staticmethod
    def convert_all(self):
        serialized_professors = {"professors": []}

        for _ in self:
            serialized_professor = ProfessorSerializer.convert_one(_)
            serialized_professors["professors"].append(serialized_professor)

        return serialized_professors

    @staticmethod
    def convert_one(self):
        serialized_professor = {
            "id": self.id,
            "name": self.name,
        }

        return serialized_professor


class AssignmentSerializer(object):
    @staticmethod
    def convert_all(self):
        serialized_assignments = {"assignments": []}

        for _ in self:
            serialized_assignment = AssignmentSerializer.convert_one(_)
            serialized_assignments["assignments"].append(serialized_assignment)

        return serialized_assignments

    @staticmethod
    def convert_one(self):

        serialized_assignments = {
            "id": self.id,
            "name": self.name,
            "course": CourseSerializer.convert_all(self.courses.all()),

        }

        return serialized_assignments

class UploadSerializer(object):
    @staticmethod
    def convert_all(self):
        serialized_assignments = {"assignments": []}

        for _ in self:
            serialized_assignment = AssignmentSerializer.convert_one(_)
            serialized_assignments["assignments"].append(serialized_assignment)

        return serialized_assignments

    @staticmethod
    def convert_one(self):

        serialized_assignments = {
            "id": self.id,
            "upload": self.upload,
            "grade": self.grade,
            "student": StudentSerializer.convert_all(self.students.all())
        }

        return serialized_assignments
