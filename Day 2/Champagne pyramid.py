def champagneTower(poured, query_row, query_glass):
    tower = [[0] * (r + 1) for r in range(102)]
    tower[0][0] = poured
    for r in range(query_row):
        for c in range(r + 1):
            overflow = (tower[r][c] - 1) / 2
            if overflow > 0:
                tower[r + 1][c] += overflow
                tower[r + 1][c + 1] += overflow
    return min(1, tower[query_row][query_glass])
# Example usage
print(champagneTower(2, 1, 1))  # Output: 0.5
