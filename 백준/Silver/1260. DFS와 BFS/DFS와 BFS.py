import sys
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for x in sorted(graph[v]):
        if not visited[x]:
            dfs(x)

def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for y in sorted(graph[x]):
            if not visited[y]:
                visited[y] = True
                queue.append(y)

n, m, v = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n + 1)
dfs(v)
print()  
visited = [False] * (n + 1)
bfs(v)
print()