import sys
from collections import deque
from itertools import combinations
import string

def bfs(x, y, n):
	color = graph[y][x]
	move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	queue = deque([(x, y)])
		
	for i in range(y, y+n):
		for j in range(x, x+n):
			if color != graph[i][j]:
				bfs(x, y, n//2)
				bfs(x+n//2, y, n//2)
				bfs(x, y+n//2, n//2)
				bfs(x+n//2, y+n//2, n//2)
				return 0
	result.append(color)
	return 0
		
input = sys.stdin.readline
result = []
n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
color = graph[0][0]
result = []
bfs(0, 0, n)
sys.stdout.write(f"{result.count(0)}\n")
sys.stdout.write(f"{result.count(1)}\n")