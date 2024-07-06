import sys
from collections import deque
from itertools import combinations
import string


n, m = map(int, sys.stdin.readline().strip().split())
data = []
for _ in range(n):
	data.append(int(sys.stdin.readline().strip()))
start = 1
end = max(data)

while start <= end:
	mid = (start + end) // 2
	count = 0
	
	for i in data:
		count += i // mid
	if count >= m:
		start = mid + 1
	else:
		end = mid - 1
sys.stdout.write(f"{end}")