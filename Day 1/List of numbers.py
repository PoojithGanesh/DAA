def process_list(numbers):
    if not numbers:
        return "The list is empty."
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1]
# Test Cases

# Test case 1: Empty list
input1 = []
output1 = process_list(input1)
print(f"Input: {input1}, Output: {output1}")
# Test case 2: Single element list
input2 = [5]
output2 = process_list(input2)
print(f"Input: {input2}, Output: {output2}")
# Test case 3: Multiple elements list
input3 = [3, 1, 9, 2, 8]
output3 = process_list(input3)
print(f"Input: {input3}, Output: {output3}")
