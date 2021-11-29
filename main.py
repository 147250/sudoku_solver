from copy import deepcopy


def check_num(matrix: list, num: int, x: int, y: int):
    if num in matrix[x]:
        return False
    for elem in matrix:
        if elem[y] == num:
            return False
    return True


class SudokuSolver:

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)
        self.empty_cell_cords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    self.empty_cell_cords.append((i, j))


if __name__ == '__main__':
    w = [[i % 2 for i in range(4)] for i in range(4)]
    q = SudokuSolver(w)
