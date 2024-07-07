import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]
for k in range(n):
	for i in range(n):
		for j in range(n):
			if graph[i][k] and graph[k][j]:
				graph[i][j] = 1
for x in graph:
	print(*x)