from collections import deque
import sys
import heapq

quiz = sys.stdin.readline().rstrip("\n")
for _ in range(int(quiz)):
	n = int(sys.stdin.readline().rstrip("\n"))
	max_q = []
	min_q = []
	removed = dict()
	for _ in range(n):
		ins, value = map(str, sys.stdin.readline().split())
		ins = ins.rstrip("\n")
		value = value.rstrip("\n")
		if ins == "I":
			heapq.heappush(max_q, -int(value))
			heapq.heappush(min_q, int(value))
			if int(value) in removed:
				removed[int(value)] += 1
			else:
				removed[int(value)] = 1
		elif ins == "D":
			if value == "1":
				while max_q and removed[-max_q[0]] == 0:
					heapq.heappop(max_q)
				if max_q:
					removed[-heapq.heappop(max_q)] -= 1
			else:
				while min_q and removed[min_q[0]] == 0:
					heapq.heappop(min_q)
				if min_q:
					removed[heapq.heappop(min_q)] -= 1
	while max_q and removed[-max_q[0]] == 0:
	        heapq.heappop(max_q)
	while min_q and removed[min_q[0]] == 0:
        	heapq.heappop(min_q)

	if not max_q or not min_q:
		sys.stdout.write("EMPTY\n")
	else:
		max_val = -max_q[0]
		min_val = min_q[0]
		sys.stdout.write(f"{max_val} {min_val}\n")