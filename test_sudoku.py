import numpy as np
from sudoku import find_next_empty, is_valid, solver
# flake8 --ignore:E201,E231
puzzle = [
    [ 3, 9,-1,   -1, 5,-1,   -1,-1,-1],
    [-1,-1,-1,    2,-1,-1,   -1,-1, 5],
    [ 4,-1,-1,    7, 1, 9,   -1, 8,-1],
    [-1, 5,-1,   -1, 6, 8,   -1,-1,-1],
    [ 2,-1, 6,   -1,-1, 3,   -1,-1,-1],
    [-1,-1,-1,   -1,-1,-1,   -1,-1, 4],
    [ 5,-1,-1,   -1,-1,-1,   -1,-1,-1],
    [ 6, 7,-1,    1,-1, 5,   -1, 4,-1],
    [ 1,-1, 9,   -1,-1,-1,    2,-1,-1]
]

expected_solution = [
    [3, 9, 1,  8, 5, 6,  4, 2, 7],
    [8, 6, 7,  2, 3, 4,  9, 1, 5],
    [4, 2, 5,  7, 1, 9,  6, 8, 3],
    [7, 5, 4,  9, 6, 8,  1, 3, 2],
    [2, 1, 6,  4, 7, 3,  5, 9, 8],
    [9, 3, 8,  5, 2, 1,  7, 6, 4],
    [5, 4, 3,  6, 9, 2,  8, 7, 1],
    [6, 7, 2,  1, 8, 5,  3, 4, 9],
    [1, 8, 9,  3, 4, 7,  2, 5, 6]
]


def test_find_next_empty():
    assert find_next_empty(puzzle) == (0, 2)
    assert find_next_empty(puzzle) != (0, 0)


def test_is_valid():
    assert is_valid(puzzle, 5, 0, 2) is False
    assert is_valid(puzzle, 6, 0, 2) is False
    assert is_valid(puzzle, 4, 0, 2) is False
    assert is_valid(puzzle, 7, 0, 2) is True


def test_solve_sudoku():
    assert solver(puzzle) is True
    assert puzzle[0][2] != -1
    assert np.array_equal(puzzle, expected_solution)
