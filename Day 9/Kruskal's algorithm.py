class UnionFind:
    def __init__(self, n):
        self.parent, self.rank = list(range(n)), [0] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1
            return True
        return False
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst, total_weight = [], 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight
# Test Case 1
edges1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst1, total_weight1 = kruskal(4, edges1)
print("Edges in MST:", mst1)  # Output: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
print("Total weight of MST:", total_weight1)  # Output: 19
