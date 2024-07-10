import sys
from collections import deque
input = sys.stdin.readline
import itertools

n, m = map(int, input().strip().split())

result = list(map(int, input().strip().split()))
result.sort()
s = list(itertools.permutations(result, m))

for x in s:
	for y in x:
		print(y, end=" ")
	print()