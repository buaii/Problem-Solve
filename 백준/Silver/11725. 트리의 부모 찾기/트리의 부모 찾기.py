import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())
data = {}
result = []
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
queue = deque([1])
visited = [False] * (n+1)

while queue:
    q = queue.popleft()
    visited[q] = True
    for x in graph[q]:
        if not visited[x]:
            queue.append(x)
            data[x] = q

for i in range(2, n+1):
    sys.stdout.write(f"{data[i]}\n")