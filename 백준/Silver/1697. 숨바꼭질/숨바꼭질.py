import sys
from collections import deque

def bfs(n):
	queue = deque([n])
	
	while queue:
		x = queue.popleft()
		if x == m:
			sys.stdout.write(f"{visited[x]}")
			return 0
		for step in (x-1, x+1, 2*x):
			if 0<= step < 100001 and not visited[step]:
				visited[step] = visited[x] + 1
				queue.append(step)

input = sys.stdin.readline

n, m = map(int, input().strip().split())
visited = [0] * 100001
bfs(n)