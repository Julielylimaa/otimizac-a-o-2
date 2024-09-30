import heapq

def prim(graph, vertices):
    mst = []
    visited = [False] * vertices
    min_heap = [(1, 1)]

    while len(mst) < vertices - 1:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        for edge_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))

        if cost != 0:
            mst.append((u, cost))

    return mst

graph_prim = {
    1: [(17, 2), (28, 3), (21, 4)],
    2: [(17, 1), (20, 3)],
    3: [(28, 1), (20, 2), (17, 8), (24, 9)],
    4: [(21, 1), (18, 5)],
    5: [(18, 4), (45, 6), (21, 11)],
    6: [(45, 5), (16, 7), (34, 11)],
    7: [(16, 6), (9, 8), (22, 15)],
    8: [(17, 3), (14, 6), (9, 7)],
    9: [(24, 3), (12, 13)],
    10: [(24, 9), (50, 12)],
    11: [(21, 5), (34, 6), (70, 21)],
    12: [(50, 10), (70, 11), (23, 17)],
    13: [(12, 9), (30, 12)],
    14: [(17, 7), (16, 15)],
    15: [(22, 7), (16, 14), (20, 16)],
    16: [(20, 15), (20, 21)],
    17: [(23, 12), (40, 14), (12, 18)],
    18: [(40, 17), (12, 19)],
    19: [(60, 20), (46, 18)],
    20: [(11, 19), (30, 16), (22, 21)],
    21: [(70, 11), (20, 16), (22, 20)]
}

vertices = 22
mst_prim = prim(graph_prim, vertices)

print("Árvore geradora mínima (Prim):")
for node, cost in mst_prim:
    print(f"Nó {node} com custo {cost}")
