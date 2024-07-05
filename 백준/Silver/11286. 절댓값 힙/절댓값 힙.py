import sys
from collections import deque
from collections import defaultdict
import heapq

n = int(sys.stdin.readline().rstrip())

min_heap = []
for i in range(n):
	command = int(sys.stdin.readline().rstrip())
	if command == 0:
		if not min_heap:
			sys.stdout.write("0\n")
		else:
			sys.stdout.write(f"{heapq.heappop(min_heap)[1]}\n")
	else:
		heapq.heappush(min_heap, (abs(command), command))