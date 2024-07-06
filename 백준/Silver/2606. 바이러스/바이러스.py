import sys
from collections import deque

def dfs(v):
	visited[v] = 1
	for nx in graph[v]:
		if visited[nx] == 0:
			dfs(nx)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
	x, y = map(int, sys.stdin.readline().rstrip().split())
	graph[x] += [y]
	graph[y] += [x]
dfs(1)
sys.stdout.write(f"{sum(visited)-1}")