from heapq import heappush, heappop

def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    pq = [(0, source)]
    visited = set()
    while pq:
        d, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heappush(pq, (nd, v))
    return dist, prev

def reconstruct_path(prev, source, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == source:
            break
        cur = prev.get(cur)
    if not path or path[-1] != source:
        return None
    return list(reversed(path))

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dist, prev = dijkstra(graph, 'A')
    path = reconstruct_path(prev, 'A', 'D')
    print("Distances:", dist)
    print("Path A->D:", path)