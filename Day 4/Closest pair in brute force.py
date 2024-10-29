'''Write a program to find the closest pair of points in a given set using the brute force approach. Analyze the time complexity of your implementation.
Define a function to calculate the Euclidean distance between two points. Implement a function to find the closest pair of points using the brute force
method. Test your program with a sample set of points and verify the correctness of your results. Analyze the time complexity of your implementation. 
Write a brute-force algorithm to solve the convex hull problem for the following set S of points? P1 (10,0)P2 (11,5)P3 (5, 3)P4 (9, 3.5)P5 (15, 3)
P6 (12.5, 7)P7 (6, 6.5)P8 (7.5, 4.5).How do you modify your brute force algorithm to handle multiple points that are lying on the sameline?'''
import math
# Closest pair using brute force
def closest_pair(points):
    min_dist = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist

# Convex hull using brute force
def convex_hull(points):
    hull = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            left = right = False
            for k in range(len(points)):
                if k != i and k != j:
                    # Calculate orientation
                    cross = (points[j][1] - points[i][1]) * (points[k][0] - points[j][0]) - \
                            (points[j][0] - points[i][0]) * (points[k][1] - points[j][1])
                    if cross > 0: left = True
                    elif cross < 0: right = True
                if left and right: break
            # Add points to hull if they form a boundary
            if not (left and right):
                if points[i] not in hull: hull.append(points[i])
                if points[j] not in hull: hull.append(points[j])
    return sorted(hull)

# Sample points
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]

# Results
pair, dist = closest_pair(points)
hull = convex_hull(points)

print("Closest pair:", pair)
print("Minimum distance:", dist)
print("Convex Hull points:", hull)

Output:
Closest pair: ((9, 3.5), (7.5, 4.5))
Minimum distance: 1.8027756377319946
Convex Hull points: [(5, 3), (6, 6.5), (10, 0), (12.5, 7), (15, 3)]
