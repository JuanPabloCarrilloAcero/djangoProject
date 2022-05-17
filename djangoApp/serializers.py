from builtins import object

class StudentSerializer(object):
    @staticmethod
    def convert_all(self):
        serialized_students = {"students": []}

        for _ in self:
            serialized_student = StudentSerializer.convert_one(_)
            serialized_students["students"].append(serialized_student)

        return serialized_students

    @staticmethod
    def convert_all_course(self):
        serialized_students = []

        for _ in self:
            serialized_student = StudentSerializer.convert_one(_)
            serialized_students.append(serialized_student)

        return serialized_students

    @staticmethod
    def convert_one(self):

        serialized_students = {
            "id": self.id,
            "name": self.name,
            "courses": CourseSerializer().convert_all(self.courses.all())
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
        serialized_courses = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "students": StudentSerializer.convert_all_course(self.students.all())
        }
        return serialized_courses

    @staticmethod
    def convert_one_student(self):
        serialized_courses = {
            "id": self.id,
            "name": self.name
        }
        return serialized_courses
