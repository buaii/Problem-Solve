import sys
from collections import deque
from itertools import combinations

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	(x, y) = map(int, sys.stdin.readline().strip().split())
	data.append((x,y))
data.sort()
for x, y in data:
	sys.stdout.write(f"{x} {y}\n")