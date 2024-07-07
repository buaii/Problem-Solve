import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
table = []
for _ in range(n):
	i, j = map(int, input().strip().split())
	table.append((i,j))
table.sort(key=lambda x: (x[1], x[0]))
result = 0
endtime = 0
for i, j in table:
	if endtime <= i:
		result += 1
		endtime = j

sys.stdout.write(f"{result}")