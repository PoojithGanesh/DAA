import itertools
def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[worker][task] for worker, task in enumerate(assignment))
def assignment_problem(cost_matrix):
    num_workers = len(cost_matrix)
    tasks = range(num_workers)
    min_cost = float('inf')
    best_assignment = None
    for assignment in itertools.permutations(tasks):
        cost = total_cost(assignment, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            best_assignment = assignment
    optimal_assignment = [(f'worker {i+1}', f'task {best_assignment[i]+1}') for i in range(num_workers)]
    return min_cost, optimal_assignment
# Test cases
cost_matrix1 = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
cost_matrix2 = [
    [15, 9, 4],
    [8, 7, 18],
    [6, 12, 11]
]
# Run the assignment problem for each test case
print("Test Case 1:")
cost1, assignment1 = assignment_problem(cost_matrix1)
print(f"Optimal Assignment: {assignment1}")
print(f"Total Cost: {cost1}")

print("\nTest Case 2:")
cost2, assignment2 = assignment_problem(cost_matrix2)
print(f"Optimal Assignment: {assignment2}")
print(f"Total Cost: {cost2}")
