def solve_n_queens(M, N, obstacles=set()):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2 and (row, col) not in obstacles
    def backtrack(row):
        if row == M:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(N):
            if is_safe(row, col):
                board[row][col] = 'Q'
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                backtrack(row + 1)
                board[row][col] = '.'
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
    board = [['.' for _ in range(N)] for _ in range(M)]
    solutions, cols, diag1, diag2 = [], set(), set(), set()
    backtrack(0)
    return solutions
# Examples
print("8x10 Board:", solve_n_queens(8, 10))
print("5x5 Board with obstacles:", solve_n_queens(5, 5, {(2, 3), (4, 1)}))
print("6x6 Board with restrictions:", solve_n_queens(6, 6, {(2, 4), (4, 2), (5, 3)}))
