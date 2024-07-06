import sys
from collections import deque

def bfs(x, y, n, m, grid):
    grid[y][x] = 0
    queue = deque([(x, y)])
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in move:
            nx, ny = cx + dx, cy + dy
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1:
                grid[ny][nx] = 0
                queue.append((nx, ny))

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    grid = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        grid[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(j, i, n, m, grid)
                count += 1

    sys.stdout.write(f"{count}\n")