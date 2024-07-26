import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
import heapq

def dfs(start, dist, visited):
    visited[start] = True
    max_dist = dist
    far_node = start
    
    for next_node, next_dist in graph[start]:
        if not visited[next_node]:
            visited[next_node] = True
            n_node, n_dist = dfs(next_node, dist + next_dist, visited)
            if max_dist < n_dist:
                max_dist = n_dist
                far_node = n_node

    return far_node, max_dist

n = int(input().strip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().strip().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

visited = [False] * (n+1)
leaf_node, _ = dfs(1, 0, visited)

visited = [False] * (n+1)
_, result = dfs(leaf_node, 0, visited)
sys.stdout.write(f"{result}")