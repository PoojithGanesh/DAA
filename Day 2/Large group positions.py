def largeGroupPositions(s):
    result = []
    start = 0
    while start < len(s):
        end = start
        while end < len(s) and s[end] == s[start]:
            end += 1
        if end - start >= 3:
            result.append([start, end - 1])
        start = end   
    return result
# Example case
s = "abbxxxxzzy"
print(largeGroupPositions(s))  # Output: [[3, 6]]
