import sys
from collections import deque
from itertools import combinations

n, k = map(int, sys.stdin.readline().strip().split())

people = [i for i in range(1, n+1)]
result = []
idx = 0
while people:
	idx += k -1
	idx = idx % len(people)
	result.append(people.pop(idx))
sys.stdout.write("<")
for x in result:
	if x == result[-1]:
		sys.stdout.write(f"{x}>")
	else:
		sys.stdout.write(f"{x}, ")