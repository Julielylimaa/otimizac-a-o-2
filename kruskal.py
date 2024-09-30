class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

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


def kruskal(graph, vertices):
    mst = []
    uf = UnionFind(vertices)

    # Ordena as arestas pelo custo
    edges = sorted(graph, key=lambda edge: edge[2])

    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))

    return mst


graph = [
    (1, 2, 17), (1, 3, 28), (1, 4, 21), (2, 3, 20),
    (3, 8, 17), (3, 9, 24), (4, 5, 18), (5, 6, 45),
    (5, 11, 21), (6, 7, 16), (6, 11, 34), (7, 15, 22),
    (8, 6, 14), (8, 7, 9), (9, 10, 24), (9, 13, 12),
    (10, 12, 50), (11, 21, 70), (12, 17, 23), (13, 12, 30),
    (14, 7, 17), (14, 15, 16), (15, 16, 20), (16, 21, 20),
    (17, 14, 40), (17, 18, 12), (18, 19, 60), (18, 20, 46),
    (19, 20, 11), (20, 16, 30), (20, 21, 22)
    
]

vertices = 22
mst_kruskal = kruskal(graph, vertices)

print("Árvore geradora mínima (Kruskal):")
for u, v, cost in mst_kruskal:
    print(f"Aresta {u} - {v} com custo {cost}")
