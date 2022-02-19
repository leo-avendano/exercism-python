class Matrix:
    def __init__(self, matrix_string):
        self.rows = list()
        for row in matrix_string.split('\n'):
            numbers = row.split(' ')
            self.rows.append([int(x) for x in numbers])
        self.columns = list()
        for column_number in range(len(self.rows[0])):
            column = list()
            for row_number in range(len(self.rows)):
                column.append(self.rows[row_number][column_number])
            self.columns.append(column)

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
