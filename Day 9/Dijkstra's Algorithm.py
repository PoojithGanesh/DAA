import heapq
def dijkstra(n, graph, source):
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]: continue
        for v in range(n):
            if graph[u][v] != float('inf'):
                new_dist = current_dist + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    return dist
# Test cases
print(dijkstra(5, [[0, 10, 3, float('inf'), float('inf')], 
                  [float('inf'), 0, 1, 2, float('inf')],
                  [float('inf'), 4, 0, 8, 2], 
                  [float('inf'), float('inf'), float('inf'), 0, 7], 
                  [float('inf'), float('inf'), float('inf'), 9, 0]], 0))  # Output: [0, 7, 3, 9, 5]
