import sys
from collections import deque
from itertools import combinations
import string

def bfs(x, y):
	visited[y][x] = True
	width[y][x] = 0
	queue = deque([(x, y)])
	move = [(0,1), (1,0), (0,-1), (-1, 0)]

	while queue:
		x, y = queue.popleft()
		for cx, cy in move:
			dx, dy	 = x + cx, y + cy
			if 0 <= dx < m and 0 <= dy < n and not visited[dy][dx] and data[dy][dx] == 1:
				visited[dy][dx] = True
				width[dy][dx] += width[y][x] + 1
				queue.append((dx, dy))

input = sys.stdin.readline
n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
width = [[0] * m for _ in range(n)]

x , y = 0, 0
for i in range(n):
	for j in range(m):
		if data[i][j] == 2:
			x, y = j, i
			break
bfs(x, y)
for i in range(n):
	for j in range(m):
		if not visited[i][j] and data[i][j] == 1:
			print(-1, end=" ")
		else:
			print(width[i][j], end=" ")
	print()
	