import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
ladder = {}
for _ in range(n):
	u, v = map(int, input().strip().split())
	ladder[u] = v
snake = {}
for _ in range(m):
	u, v = map(int, input().strip().split())
	snake[u] = v
queue = deque([1])
visited = [False] * 101
count = [0] * 101
while queue:
	q = queue.popleft()
	for i in range(1,7):
		next = q + i
		if next <= 100:
			if next in ladder:
				next = ladder[next]
			if next in snake:
				next = snake[next] 
			if not visited[next]:
				visited[next] = True
				queue.append(next)
				count[next] = count[q] + 1
				if next == 100:
					sys.stdout.write(f"{count[100]}")
					exit()
sys.stdout.write(f"{count[100]}")