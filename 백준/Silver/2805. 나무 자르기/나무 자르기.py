import sys
from collections import deque
from itertools import combinations
import string

input = sys.stdin.readline
n, m = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

start, end = 1, sum(data)
result = 0
while start <= end:
	count = 0
	mid = (start + end) // 2
	for d in data:
		if d > mid:
			count += d - mid
	if count >= m:
		start = mid + 1
	else:
		result = mid - 1
		end = mid - 1
sys.stdout.write(f"{result}")