import sys
from collections import deque
input = sys.stdin.readline

def count(q, command):
	if command == "D":
		q = (q * 2) % 10000				
	elif command == "S":
		if q == 0:
			q = 9999				
		else:
			q = q - 1
	elif command == "L":
		q = (10 * q + (q // 1000)) % 10000
	else:
		q =  (((q % 10) * 1000) + (q // 10)) % 10000
	return q

def bfs(n):
	code = ['D', 'S', 'L', 'R']
	queue = deque([n])
	visited[n] = True
	while queue:
		q = queue.popleft()

		for x in code:
			next = count(q, x)
			if not visited[next]:
				visited[next] = True
				queue.append(next)
				result[next].append(''.join(result[q]) + x)

			if next == int(v):
				return 0

			

t = int(input().strip())

for _ in range(t):
	u, v = map(str, input().strip().split())
	visited = [False for _ in range(10001)]
	result = [[] for _ in range(10001)]
	bfs(int(u))
	print(*result[int(v)])