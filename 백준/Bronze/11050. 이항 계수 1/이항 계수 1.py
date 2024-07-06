import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())
data = []
for i in range(n):
	data.append(i)
result = 0
for x in combinations(data, m):
	result += 1
sys.stdout.write(f"{result}")