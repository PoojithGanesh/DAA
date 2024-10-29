import itertools
def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][task] for i, task in enumerate(assignment))
def assignment_problem(cost_matrix):
    min_cost, best_assignment = float('inf'), None
    for assignment in itertools.permutations(range(len(cost_matrix))):
        cost = total_cost(assignment, cost_matrix)
        if cost < min_cost:
            min_cost, best_assignment = cost, assignment
    return min_cost, [(f'worker {i+1}', f'task {task+1}') for i, task in enumerate(best_assignment)]

# Test cases
cost_matrix1 = [[3, 10, 7], [8, 5, 12], [4, 6, 9]]
cost_matrix2 = [[15, 9, 4], [8, 7, 18], [6, 12, 11]]
# Results
print("Test Case 1:", assignment_problem(cost_matrix1))
print("Test Case 2:", assignment_problem(cost_matrix2))
