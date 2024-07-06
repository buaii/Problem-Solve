import sys
from collections import deque
from itertools import combinations
import string


n, m = map(int, sys.stdin.readline().strip().split())
data_n = set()
for _ in range(n):
	data_n.add(sys.stdin.readline().strip())
data_m = set()
for _ in range(m):
	data_m.add(sys.stdin.readline().strip())	
result = []
for i in data_n:
	if i in data_m:
		result.append(i)
result.sort()
sys.stdout.write(f"{len(result)}\n")
for i in result:
	sys.stdout.write(f"{i}\n")