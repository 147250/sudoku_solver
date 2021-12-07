from copy import deepcopy


def check_num(matrix: list, num: int, row: int, column: int):
    """Checks if there is such a number horizontally and vertically in the matrix"""

    horizontal = matrix[row]
    vertical = [elem[column] for elem in matrix]
    if horizontal.count(num) == vertical.count(num) == 0:
        return True

    return False


class SudokuSolver:
    """Create an instance by passing a 9x9 matrix as the only argument and start the method run"""

    def __init__(self, matrix: list):
        self.matrix = deepcopy(matrix)
        self.empty_cell_cords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    self.empty_cell_cords.append((i, j))

    def run(self):
        pos = 0
        while -1 < pos < len(self.empty_cell_cords):
            i, j = self.empty_cell_cords[pos]
            num = self.matrix[i][j] + 1
            self.matrix[i][j] = 0
            check = check_num(self.matrix, num, i, j)

            while num < 10 and not check:
                num += 1
                check = check_num(self.matrix, num, i, j)

            if num < 10:
                self.matrix[i][j] = num
                pos += 1
            else:
                pos -= 1

        if pos == len(self.empty_cell_cords):
            return self.matrix
        else:
            return f"No solution"
