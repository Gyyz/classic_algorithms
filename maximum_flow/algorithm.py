from collections import deque

def edmonds_karp(capacity, source, sink):
    """
    capacity: dict[u][v] -> capacity (nonnegative)
    Returns (max_flow_value, residual_capacities)
    """
    nodes = set(capacity.keys()) | {v for u in capacity for v in capacity[u]}
    residual = {u: {} for u in nodes}
    for u in capacity:
        for v, c in capacity[u].items():
            residual[u][v] = c
            residual.setdefault(v, {})
            residual[v].setdefault(u, 0)

    max_flow = 0
    while True:
        parent = {source: None}
        bottleneck = {source: float('inf')}
        q = deque([source])
        found = False
        while q and not found:
            u = q.popleft()
            for v, c in residual[u].items():
                if c > 0 and v not in parent:
                    parent[v] = u
                    bottleneck[v] = min(bottleneck[u], c)
                    if v == sink:
                        found = True
                        break
                    q.append(v)
        if not found:
            break

        flow = bottleneck[sink]
        max_flow += flow
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] = residual[v].get(u, 0) + flow
            v = u
    return max_flow, residual

if __name__ == "__main__":
    # Simple demo network
    capacity = {
        's': {'a': 3, 'b': 2},
        'a': {'b': 1, 't': 2},
        'b': {'t': 3},
        't': {}
    }
    max_flow, residual = edmonds_karp(capacity, 's', 't')
    print("Max flow:", max_flow)