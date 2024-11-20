def k_closest(points, k):
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
# Test cases
print(k_closest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))  # Output: [[-2, 2], [0, 1]]
