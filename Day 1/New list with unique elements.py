def get_unique_elements(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers

# Example usage:
numbers = [3, 1, 9, 2, 8, 3, 9, 1]
unique_numbers = get_unique_elements(numbers)
print(f"Original list: {numbers}")
print(f"Unique elements: {unique_numbers}")
