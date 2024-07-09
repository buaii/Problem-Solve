import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
	visited[x][y] = True
	queue = deque([(x, y)])
	move = [(1,0), (0,1), (0, -1), (-1,0)]

	while queue:
		x, y = queue.popleft()

		for cx, cy in move:
			dx, dy = x + cx, y + cy
			if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and graph[dx][dy]:
				visited[dx][dy] = True
				distance[dx][dy] = distance[x][y] + 1
				if dx == n-1 and dy == m-1:		
					return 0
				queue.append((dx, dy))
				
n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
distance = [[1] * m for _ in range(n)]

bfs(0,0)
sys.stdout.write(f"{distance[n-1][m-1]}")