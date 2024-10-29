import itertools
def total_value(items, values):
    return sum(values[i] for i in items)
def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity
def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_selection = []
    for r in range(n + 1):
        for items in itertools.combinations(range(n), r):
            if is_feasible(items, weights, capacity):
                value = total_value(items, values)
                if value > max_value:
                    max_value = value
                    best_selection = items
    return list(best_selection), max_value
# Test cases
weights1 = [2, 3, 1]
values1 = [4, 5, 3]
capacity1 = 4
weights2 = [1, 2, 3, 4]
values2 = [2, 4, 6, 3]
capacity2 = 6

# Results
print("Test Case 1:")
selection1, value1 = knapsack(weights1, values1, capacity1)
print(f"Optimal Selection: {selection1}")
print(f"Total Value: {value1}")

print("\nTest Case 2:")
selection2, value2 = knapsack(weights2, values2, capacity2)
print(f"Optimal Selection: {selection2}")
print(f"Total Value: {value2}")
