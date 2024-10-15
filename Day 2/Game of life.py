def gameOfLife(board):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                    live_neighbors += 1
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 2  
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 3 
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  
            if board[i][j] == 3:
                board[i][j] = 1 
# Example usage
board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]
gameOfLife(board)
print(board)
