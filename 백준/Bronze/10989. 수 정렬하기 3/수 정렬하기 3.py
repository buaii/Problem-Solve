import sys
from collections import deque
from itertools import combinations
import string

n = int(sys.stdin.readline().strip())
arr = [0] * (10001)
for _ in range(n):
	arr[int(sys.stdin.readline().strip())] += 1
for idx, x in enumerate(arr):
	if x != 0:
		for _ in range(x):
			sys.stdout.write(f"{idx}\n")