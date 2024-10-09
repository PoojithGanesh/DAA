def rob(houses):
    if len(houses) == 1:
        return houses[0]
    def rob_line(houses):
        prev, curr = 0, 0
        for money in houses:
            prev, curr = curr, max(curr, prev + money)
        return curr
    case1 = rob_line(houses[:-1])
    case2 = rob_line(houses[1:])
    return max(case1, case2)

# Example usage
houses = [2, 3, 2]
print(rob(houses))  # Output: 3
houses = [1, 2, 3, 1]
print(rob(houses))  # Output: 4
