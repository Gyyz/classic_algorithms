from heapq import nlargest

def beam_search(graph, start, is_goal, score_fn, beam_width=3, max_depth=50):
    beam = [(score_fn([start]), [start])]
    for depth in range(max_depth):
        candidates = []
        for score, path in beam:
            node = path[-1]
            if is_goal(node):
                return path
            for nb in graph.get(node, []):
                new_path = path + [nb]
                candidates.append((score_fn(new_path), new_path))
        if not candidates:
            break
        beam = nlargest(beam_width, candidates, key=lambda x: x[0])
    return None

if __name__ == "__main__":
    graph = {
        'S': ['A','B'],
        'A': ['C','D'],
        'B': ['D','E'],
        'C': ['G'],
        'D': ['G'],
        'E': ['F'],
        'F': ['G'],
        'G': []
    }
    goal = 'G'
    def is_goal(n):
        return n == goal
    def score_fn(path):
        # Favor shorter paths and nodes closer to goal (toy score)
        last = path[-1]
        dist = ord('G') - ord(last)
        return max(0, 100 - len(path)*10 - dist)
    p = beam_search(graph, 'S', is_goal, score_fn, beam_width=2)
    print("Beam search path:", p)