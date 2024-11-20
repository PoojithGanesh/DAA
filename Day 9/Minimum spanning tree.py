class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)    
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2]) 
    uf = UnionFind(n)
    mst = []
    mst_weight = 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            mst_weight += w
    return mst, mst_weight
# Example usage:
edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]
n = 4  # Number of nodes
mst, mst_weight = kruskal(n, edges)
print("Edges in MST:", mst)  # Minimum Spanning Tree edges
print("Total weight of MST:", mst_weight)  # Total weight of MST
