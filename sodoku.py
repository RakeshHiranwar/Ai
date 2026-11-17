board = [
    [8, 0, 2, 0, 0, 3, 5, 1, 0],
    [0, 6, 0, 0, 9, 1, 0, 0, 3],
    [7, 0, 1, 0, 0, 0, 8, 9, 4],

    [6, 0, 8, 0, 0, 4, 0, 2, 1],
    [0, 0, 0, 2, 5, 8, 0, 6, 0],
    [9, 2, 0, 3, 1, 0, 4, 0, 0],

    [0, 0, 0, 4, 0, 2, 7, 8, 0],
    [0, 0, 5, 0, 8, 9, 0, 0, 0],
    [2, 0, 0, 0, 0, 7, 1, 0, 0]
]


# Check whether a number is valid
def isSafe(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    sr = (row // 3) * 3
    sc = (col // 3) * 3

    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == num:
                return False

    return True


# Constraint Propagation
def propagate(board):

    for r in range(9):
        for c in range(9):

            if board[r][c] == 0:

                possible = [n for n in range(1, 10)
                            if isSafe(board, r, c, n)]

                if len(possible) == 0:
                    return False

                if len(possible) == 1:
                    board[r][c] = possible[0]
                    return propagate(board)

    return True


# Backtracking
def solve(board):

    if not propagate(board):
        return False

    for r in range(9):
        for c in range(9):

            if board[r][c] == 0:

                for num in range(1, 10):

                    if isSafe(board, r, c, num):

                        board[r][c] = num

                        if solve(board):
                            return True

                        board[r][c] = 0

                return False

    return True


# Main program
if solve(board):
    for row in board:
        print(row)
else:
    print("No solution exists")