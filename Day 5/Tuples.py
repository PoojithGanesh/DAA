from collections import defaultdict
def four_sum_count(A, B, C, D):
    sum_ab = defaultdict(int)
    # Store sums of A[i] + B[j] in sum_ab
    for i in A:
        for j in B:
            sum_ab[i + j] += 1 
    count = 0
    # For each sum C[k] + D[l], check if the negative exists in sum_ab
    for k in C:
        for l in D:
            count += sum_ab[-(k + l)]
    return count
# Test cases
A1 = [1, 2]
B1 = [-2, -1]
C1 = [-1, 2]
D1 = [0, 2]
print(four_sum_count(A1, B1, C1, D1))  # Output: 2
A2 = [0]
B2 = [0]
C2 = [0]
D2 = [0]
print(four_sum_count(A2, B2, C2, D2))  # Output: 1
