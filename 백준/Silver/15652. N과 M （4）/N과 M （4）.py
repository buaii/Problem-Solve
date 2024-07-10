import sys
from collections import deque
input = sys.stdin.readline
import itertools

n, m = map(int, input().strip().split())

result = []
for i in range(1, n+1):
	result.append(i)
s = list(itertools.combinations_with_replacement(result, m))

for x in s:
	for y in x:
		print(y, end=" ")
	print()