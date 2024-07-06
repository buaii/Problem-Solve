import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())
data = list(sys.stdin.readline().strip().split())
data_final = []
for x in data:
	data_final.append(int(x))
result = 0
for cards in combinations(data_final, 3):
	if sum(cards) <= m:
		result = max(result, sum(cards))
sys.stdout.write(f"{result}")