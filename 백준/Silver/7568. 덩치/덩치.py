import sys
from collections import deque
from itertools import combinations
import string

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	x, y = map(int ,sys.stdin.readline().strip().split())
	data.append((x,y))
res = []
for i_x, i_y in data:
	count = 1
	for j_x, j_y in data:
		if j_x > i_x and j_y > i_y:
			count += 1
	
	sys.stdout.write(f"{count} ")

		