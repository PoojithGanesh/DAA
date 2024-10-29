import math
points=[(1,2), (4,5), (7,8), (3,1)]
min_distance=float('inf')
closest_pair=()
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance =math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1])**2)
        if distance<min_distance:
            min_distance=distance
            closest_pair=(points[i], points[j])

print("Closest pair:", closest_pair[0], "-", closest_pair[1])
print("Minimum distance: ", min_distance)

Output:
Closest pair: ((1, 2), (3, 1))
Minimum distance: 2.23606797749979
