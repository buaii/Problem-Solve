import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
	visited = [False] * (n+1)
	queue = deque([(start, 0)])
	
	while queue:
		current, distance = queue.popleft()
		
		if current == end:
			return distance
		if not visited[current]:
			visited[current] = True
			for neighbor in graph[current]:
				if not visited[neighbor]:
					queue.append((neighbor, distance + 1))

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0
answer = [sys.maxsize]

for _ in range(m):
	a, b = map(int, input().strip().split())
	graph[a].append(b)
	graph[b].append(a)

for i in range(1, n+1):
	result = 0
	for j in range(1, n+1):
		if j != i:
			result += bfs(i, j)
	answer.append(result)
print(answer.index(min(answer)))