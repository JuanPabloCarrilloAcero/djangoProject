from builtins import object

class StudentSerializer(object):
    @staticmethod
    def convert_all(self, add_nesting=True):
        serialized_students = {"students": []}

        for _ in self:
            serialized_student = StudentSerializer.convert_one(_)
            serialized_students["students"].append(serialized_student)

        return serialized_students

    @staticmethod
    def convert_all_course(self, add_nesting=True):
        serialized_students = []

        for _ in self:
            serialized_student = StudentSerializer.convert_one(_)
            serialized_students.append(serialized_student)

        return serialized_students

    @staticmethod
    def convert_one(self, add_nesting=True):

        serialized_students = {
            "id": self.id,
            "name": self.name,
        }
        if add_nesting:
            serialized_students["courses"] = CourseSerializer().convert_all(self.courses.all(), False)
        return serialized_students

class CourseSerializer(object):

    @staticmethod
    def convert_all(self, add_nesting=True):
        serialized_courses = {"courses": []}

        for _ in self:
            serialized_course = CourseSerializer.convert_one(_, add_nesting)
            serialized_courses["courses"].append(serialized_course)

        return serialized_courses

    @staticmethod
    def convert_one(self, add_nesting=True):
        serialized_courses = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
        if add_nesting:
            serialized_courses["students"] = StudentSerializer.convert_all_course(self.students.all(), False)
        return serialized_courses

    @staticmethod
    def convert_one_student(self):
        serialized_courses = {
            "id": self.id,
            "name": self.name
        }
        return serialized_courses
