DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
                    'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANTS = {
    "V": "Violets",
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes"
}

PLANTS_PER_STUDENT = 4


class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.asigned_plants = dict()
        students.sort()
        first_row, second_row = diagram.split('\n')

        for index, student in enumerate(students):
            if index > round(len(first_row)/2) - 1:
                break
            first_plant = PLANTS[first_row[index*2]]
            second_plant = PLANTS[first_row[index*2 + 1]]
            third_plant = PLANTS[second_row[index*2]]
            fourth_plant = PLANTS[second_row[index*2 + 1]]
            self.asigned_plants[student] = [first_plant,
                                            second_plant,
                                            third_plant,
                                            fourth_plant]

    def plants(self, student):
        return self.asigned_plants[student]
