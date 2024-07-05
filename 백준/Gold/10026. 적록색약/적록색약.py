import sys
from collections import deque

sys.setrecursionlimit(10**6)

def bfs(x, y, color, grid, visited, n):
	move = [(0,1), (0,-1), (1,0), (-1,0)]
	queue = deque([(x, y)])	
	visited[x][y] = True
	
	while queue:
		cx, cy = queue.popleft()
		for dx, dy in move:
			nx, ny = cx + dx, cy + dy
			if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
				if grid[nx][ny] == color:
					visited[nx][ny] = True
					queue.append((nx, ny))

def count_area(grid, n, is_color_blind):
	visited = [[False] * n for _ in range(n)]
	count = 0
	
	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				if is_color_blind and grid[i][j] in 'RG':
					color = 'R'
				else:
					color = grid[i][j]
				bfs(i, j, color, grid, visited, n)
				count += 1
	return count

n = int(sys.stdin.readline().rstrip())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
normal = count_area(grid, n, False)
for i in range(n):
	for j in range(n):
		if grid[i][j] == 'G':
			grid[i][j] = 'R'
blind = count_area(grid, n, True)

sys.stdout.write(f"{normal} {blind}")