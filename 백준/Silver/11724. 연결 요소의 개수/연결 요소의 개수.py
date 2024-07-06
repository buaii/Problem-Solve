import sys
from collections import deque
from itertools import combinations
import string

def bfs(x):
	queue = deque([x])
	visited[x] = True
	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			if not visited[neighbor]:
				visited[neighbor] = True
				queue.append(neighbor)

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	u, v = map(int, input().strip().split())
	graph[u].append(v)
	graph[v].append(u)

count = 0
for x in range(1, len(graph)):
	if not visited[x]:
		count += 1
		bfs(x)	
sys.stdout.write(f"{count}")