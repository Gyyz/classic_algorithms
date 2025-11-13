from heapq import heappush, heappop

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def neighbors(r, c):
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                yield nr, nc

    def h(p):
        return abs(p[0]-goal[0]) + abs(p[1]-goal[1])

    open_heap = []
    heappush(open_heap, (h(start), 0, start, None))  # (f, g, node, parent)
    came_from = {}
    best_g = {start: 0}

    while open_heap:
        f, g, node, parent = heappop(open_heap)
        if node in came_from:
            continue
        came_from[node] = parent
        if node == goal:
            # reconstruct path
            path = []
            cur = node
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return list(reversed(path))
        for nb in neighbors(*node):
            ng = g + 1
            if nb not in best_g or ng < best_g[nb]:
                best_g[nb] = ng
                heappush(open_heap, (ng + h(nb), ng, nb, node))
    return None

def render_grid(grid, path=None, start=None, goal=None):
    rows, cols = len(grid), len(grid[0])
    path_set = set(path or [])
    lines = []
    for r in range(rows):
        line = []
        for c in range(cols):
            cell = grid[r][c]
            pos = (r, c)
            if pos == start:
                ch = 'S'
            elif pos == goal:
                ch = 'G'
            elif cell == 1:
                ch = '#'
            elif pos in path_set:
                ch = '*'
            else:
                ch = '.'
            line.append(ch)
        lines.append(''.join(line))
    return '\n'.join(lines)

if __name__ == "__main__":
    grid = [
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,1,0],
        [0,1,0,0,0],
        [0,0,0,1,0],
    ]
    start = (0,0)
    goal = (4,4)
    path = a_star(grid, start, goal)
    print("A* path:", path)
    print("\nGrid visualization:")
    print(render_grid(grid, path=path, start=start, goal=goal))