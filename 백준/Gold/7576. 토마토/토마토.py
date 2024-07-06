import sys
from collections import deque

def bfs(queue):
	move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	
	while queue:
		x, y = queue.popleft()
		for cx, cy in move:
			dx, dy = x + cx, y + cy
			if 0 <= dx < m and 0 <= dy < n and not visited[dy][dx] and data[dy][dx] == 0:
				visited[dy][dx] = True
				width[dy][dx] = width[y][x] + 1
				queue.append((dx, dy))

input = sys.stdin.readline
m, n = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
width = [[0] * m for _ in range(n)]

queue = deque([])
for i in range(n):
	for j in range(m):
		if data[i][j] == 1:
			queue.append((j, i))
			visited[i][j] = True

bfs(queue)

max_days = 0
for i in range(n):
	for j in range(m):
		if data[i][j] == 0 and not visited[i][j]:
			print(-1)
			exit(0)
		max_days = max(max_days, width[i][j])

print(max_days)
