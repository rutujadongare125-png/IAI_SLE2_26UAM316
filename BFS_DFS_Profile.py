from collections import deque
import time
import timeit

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(start, goal):
    q = deque([start])
    visited = {start}
    nodes = 0

    while q:
        node = q.popleft()
        nodes += 1

        if node == goal:
            return nodes

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return nodes


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes += 1

        if node == goal:
            return nodes

        for nxt in reversed(graph[node]):
            if nxt not in visited:
                stack.append(nxt)

    return nodes


print("BFS nodes:", bfs('A', 'F'))
print("DFS nodes:", dfs('A', 'F'))
print("Profiling BFS and DFS for 30 seconds...")

end_time = time.perf_counter() + 30

while time.perf_counter() < end_time:
    bfs('A', 'F')
    dfs('A', 'F')

print("Profiling finished.")