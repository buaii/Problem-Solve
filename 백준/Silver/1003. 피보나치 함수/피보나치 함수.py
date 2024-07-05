import sys
from collections import deque
from collections import defaultdict


def febo(n, zero, one):
	temp1, temp2, temp3 = 0, 1, 0
	if n == 0:
		zero[0] += 1
		return 0
	elif n == 1:
		one[0] += 1
		return 0
	else:
		for i in range(1, n):
			temp3 = temp1 + temp2
			temp1 = temp2
			temp2 = temp3
		zero[0] = temp1
		one[0] = temp2
	return 0

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
	data = []
	zero, one = [0], [0]
	s = int(sys.stdin.readline().rstrip())
	febo(s, zero, one)
	sys.stdout.write(f"{zero[0]} {one[0]}\n")