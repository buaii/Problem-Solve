import sys
from collections import deque

n = int(sys.stdin.readline().strip())
for _ in range(n):
	stack = []
	input_data = list(sys.stdin.readline().strip())
	check  = True
	for x in input_data:
		if x == "(":
			stack.append(x)
		else:
			if stack:
				stack.pop()
			else:		
				check = False
				break
	if stack:
		check = False
	if not check:
		sys.stdout.write("NO\n")
	else:	
		sys.stdout.write("YES\n")