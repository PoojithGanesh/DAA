def max_weight_greedy(weights, max_capacity):
    weights.sort(reverse=True)
    current_weight = 0
    for weight in weights:
        if current_weight + weight <= max_capacity:
            current_weight += weight
        else:
            break 
    return current_weight
# Test Case 1
weights1 = [10, 20, 30, 40, 50]
max_capacity1 = 60
print(max_weight_greedy(weights1, max_capacity1))  # Output: 50
