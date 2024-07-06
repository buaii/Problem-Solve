import sys
from collections import deque
from itertools import combinations

n = int(sys.stdin.readline().strip())
data = list(sys.stdin.readline().strip().split())
real_data = {}
for x in data:
	if x in real_data:
		real_data[x] += 1
	else:
		real_data[x] = 1
m = int(sys.stdin.readline().strip())
check = list(sys.stdin.readline().strip().split())


for x in check:
	if x in real_data:
		sys.stdout.write(f"{real_data[x]} ")
	else:
		sys.stdout.write("0 ")