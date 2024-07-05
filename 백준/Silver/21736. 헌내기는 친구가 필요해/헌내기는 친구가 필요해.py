import sys
from collections import deque

def bfs(start_x, start_y, grid, visited):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    people_count = 0
    
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 'P':
            people_count += 1
            
        for cx, cy in move:
            dx, dy = x + cx, y + cy
            if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and grid[dx][dy] != 'X':
                visited[dx][dy] = True
                queue.append((dx, dy))
    
    return people_count

# Read input
n, m = map(int, sys.stdin.readline().rstrip().split())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))

# Directions for moving: down, right, up, left
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Find Do-yeon's starting position and initialize visited array
visited = [[False] * m for _ in range(n)]
start_x, start_y = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'I':
            start_x, start_y = i, j
            break
    if start_x != -1:
        break

# Perform BFS to find the number of people Do-yeon can meet
people_count = bfs(start_x, start_y, grid, visited)

# Output the result
if people_count == 0:
    sys.stdout.write("TT\n")
else:
    sys.stdout.write(f"{people_count}\n")
