count=0

def isSafe(board, row, col, n):
    # horizontal
    for j in range(n):
        if board[row][j] == 'Q':
            return False
    
    # vertical
    for i in range(n):
        if board[i][col] == 'Q':
            return False
            
    # left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
        
    # right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
        
    return True

def nQueens(board, row, n):
    global count
    if row == n:
        # Print each solution directly
        count += 1
        print(" Solution ",count)
        for r in board:
            print(*r)
        print()
        return

    for j in range(n):
        if isSafe(board, row, j, n):
            board[row][j] = 'Q'
            nQueens(board, row + 1, n)
            board[row][j] = '.'

def solveNQueens(n):
    board = []
    for i in range(n):
        row=["."]*n
        board.append(row)

    nQueens(board, 0, n)

solveNQueens(8)