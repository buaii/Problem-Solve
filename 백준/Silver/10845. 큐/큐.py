import sys
from collections import deque
from itertools import combinations

n = int(sys.stdin.readline().strip())
q = deque()
for _ in range(n):
	command = list(sys.stdin.readline().strip().split())
	if command[0] == "push":
		q.append(int(command[1]))
	elif command[0] == "pop":
		if q:
			sys.stdout.write(f"{q.popleft()}\n")
		else:
			sys.stdout.write(f"-1\n")	
	elif command[0] == "size":
		sys.stdout.write(f"{len(q)}\n")
	elif command[0] == "empty":
		if q:
			sys.stdout.write(f"0\n")
		else:
			sys.stdout.write(f"1\n")	
	elif command[0] == "front":
		if q:
			sys.stdout.write(f"{q[0]}\n")
		else:
			sys.stdout.write(f"-1\n")	
	elif command[0] == "back":
		if q:
			sys.stdout.write(f"{q[-1]}\n")
		else:
			sys.stdout.write(f"-1\n")	