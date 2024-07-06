import sys
from collections import deque
from itertools import combinations
import string


n, m = map(int, sys.stdin.readline().strip().split())

data = list(sys.stdin.readline().strip().split())
pre_sum = [0]
sum = 0
for x in data:
	sum += int(x)
	pre_sum.append(sum)

for _ in range(m):
	i, j = map(int, sys.stdin.readline().strip().split())
	sys.stdout.write(f"{pre_sum[j] - pre_sum[i-1]}\n")
