import sys
from collections import deque
input = sys.stdin.readline

def checkBoard(x, y):
	if 0 <= x < n and 0 <= y < m:
		return True
	else:
		return False

n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0
check = [
# l # ㅡ
	[(0,0), (1,0), (2,0), (3,0)], [(0,0), (0,1), (0,2), (0,3)],
# ㅁ
	[(0,0), (1,0), (0,1), (1,1)],
# ㄱ # ㄴ # ㄴ90 # ㄱ90
	[(0,0), (0,1), (1,1), (2,1)], [(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (0,2), (-1,2)],
	[(0,0), (1,0), (0,1), (0,2)],
	[(0,0), (1,0), (2,0), (2,-1)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (1,0), (2,0)],
	[(0,0), (1,0), (1,1), (1,2)],
# ㄴㄱ # ㄴㄱ90 
	[(0,0), (1,0), (1,1), (2,1)], [(0,0), (0,1), (-1,1), (-1,2)],
	[(0,0), (1,0), (1,-1), (2,-1)], [(0,0), (0,1), (1,1), (1,2)],
# ㅜ # ㅏ # ㅗ # ㅓ
	[(0,0), (0,1), (1,1), (0,2)], [(0,0), (1,0), (1,1), (2,0)], 
	[(0,0), (0,1), (-1,1), (0,2)], [(0,0), (1,0), (1,-1), (2,0)]
	]
answer = 0
for x in range(n):
	for y in range(m):
		for c in check:
			point = True
			sum = 0
			for cx, cy in c:
				dx, dy = x + cx, y + cy
				if not checkBoard(dx, dy):
					point = False
					break
				else:
					sum += graph[dx][dy]
			if point:
				answer = max(answer, sum)

sys.stdout.write(f"{answer}")