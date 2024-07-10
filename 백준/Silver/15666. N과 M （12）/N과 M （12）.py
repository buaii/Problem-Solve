import sys
from collections import deque
input = sys.stdin.readline
import itertools

n, m = map(int, input().strip().split())

result = list(map(int, input().strip().split()))
result.sort()
s = list(itertools.combinations_with_replacement(result, m))

result = []
for x in s:
	if x not in result:
		result.append(x)

for x in result:
	for s in x:
		print(s, end=" ")
	print()