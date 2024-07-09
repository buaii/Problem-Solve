import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
	visited[x][y] = True
	count = 1
	queue = deque([(x,y)])
	move = [(1,0), (0,1), (-1,0), (0,-1)]

	while queue:
		cx, cy = queue.popleft()		
		for bx, by in move:
			dx, dy = cx + bx, cy + by
			if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy] and graph[dx][dy] == '1':
				count += 1
				visited[dx][dy] = True
				queue.append((dx, dy))
	return count

n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []
for x in range(n):
	for y in range(n):
		if graph[x][y] == '1' and not visited[x][y]:
			result.append(bfs(x, y))
result.sort()
sys.stdout.write(f"{len(result)}\n")
for x in result:
	sys.stdout.write(f"{x}\n")
	