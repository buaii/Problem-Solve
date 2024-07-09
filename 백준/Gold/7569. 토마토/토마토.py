import sys
from collections import deque
input = sys.stdin.readline

def bfs():	
	move = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

	while queue:
		x, y, z= queue.popleft()
		for cx, cy, cz in move:
			dx, dy, dz = x + cx, y + cy, z + cz
			if 0 <= dx < n and 0 <= dy < m and 0 <= dz < l and not visited[dz][dy][dx] and graph[dz][dy][dx] == "0":
				visited[dz][dy][dx] = True
				graph[dz][dy][dx] = "1"
				date[dz][dy][dx] = date[z][y][x] + 1
				queue.append((dx, dy, dz))
	
n, m, l = map(int, input().strip().split())

graph = [[input().strip().split() for _ in range(m)] for _ in range(l)]
visited = [[[False] * n for _ in range(m)] for _ in range(l)]
date = [[[0] * n for _ in range(m)] for _ in range(l)]
queue = deque([])
for z in range(l):
	for y in range(m):
		for x in range(n):
			if graph[z][y][x] == "1":
				visited[z][y][x] = True
				queue.append((x, y, z))

bfs()
check = True
max_date = 0
for z in range(l):
	for y in range(m):
		for x in range(n):
			if graph[z][y][x] == "0":
				sys.stdout.write("-1\n")
				check = False
				break
			max_date = max(max_date, date[z][y][x])
		if not check:
			break

if check:
    sys.stdout.write(f"{max_date}\n")
			