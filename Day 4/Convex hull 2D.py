def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
def convex_hull(points):
    if len(points) < 3:
        return None
    hull = []
    start = min(points, key=lambda p: p[0])
    p = start
    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if q == p or orientation(p, q, r) < 0:
                q = r
        p = q
        if p == start:
            break
    return hull
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
print("Convex Hull:", convex_hull(points))
