def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    first = 1
    second = 2
    for i in range(3, n+1):
        third = first + second
        first = second
        second = third
    return second
# Example cases
print(climbStairs(4))  # Output: 5
print(climbStairs(3))  # Output: 3
