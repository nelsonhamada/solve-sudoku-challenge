from pprint import pprint


def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column

    return None, None


def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # Anteriormente feito a verificação com if < 3... Porém ao pesquisar sobre
    # outras soluções achei essa bem mais interessante e reduzida.
    row_square_check = (row // 3) * 3
    col_square_check = (col // 3) * 3

    for row_check in range(row_square_check, row_square_check + 3):
        for column_check in range(col_square_check, col_square_check + 3):
            if puzzle[row_check][column_check] == guess:
                return False

    return True


def solver(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solver(puzzle):
                return True
        puzzle[row][col] = -1
    return False


if __name__ == '__main__':
    example_board = [
      [2, 5, -1, -1, 3, -1, 9, -1, 1],
      [-1, 1, -1, -1, -1, 4, -1, -1, -1],
      [4, -1, 7, -1, -1, -1, 2, -1, 8],
      [-1, -1, 5, 2, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, 9, 8, 1, -1, -1],
      [-1, 4, -1, -1, -1, 3, -1, -1, -1],
      [-1, -1, -1, 3, 6, -1, -1, 7, 2],
      [-1, 7, -1, -1, -1, -1, -1, -1, 3],
      [9, -1, 3, -1, -1, -1, 6, -1, 4]
    ]
    print(solver(example_board))
    pprint(example_board)
