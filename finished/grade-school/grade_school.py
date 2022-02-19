class School:
    def __init__(self):
        self.students = dict()
        self.grades = dict()
        self.operations = list()

    def add_student(self, name, grade):
        if self.students.get(name) == None:
            self.students[name] = grade
            if self.grades.get(grade) == None:
                self.grades[grade] = [name]
            else:
                self.grades[grade].append(name)
            self.operations.append(True)
        else:
            self.operations.append(False)

    def roster(self):
        students = list()
        grades = [*self.grades.keys()]
        grades.sort()
        for grade in grades:
            self.grades[grade].sort()
            students += self.grades[grade]
        return students

    def grade(self, grade_number):
        result = []
        for (student, grade) in self.students.items():
            if grade == grade_number:
                result.append(student)
        result.sort()
        return result

    def added(self):
        return self.operations
