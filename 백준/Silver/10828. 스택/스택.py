import sys
from collections import deque

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	input_data = sys.stdin.readline().strip().split()

	if input_data[0] == "push":
		data.append(input_data[1])
	elif input_data[0] == "pop":
		if data:
			sys.stdout.write(f"{data.pop()}\n")
		else:
			sys.stdout.write(f"-1\n")
	elif input_data[0] == "size":
		sys.stdout.write(f"{len(data)}\n")		
	elif input_data[0] == "empty":
		if data:
			sys.stdout.write(f"{0}\n")
		else:
			sys.stdout.write(f"1\n")
	elif input_data[0] == "top":
		if data:
			sys.stdout.write(f"{data[-1]}\n")
		else:
			sys.stdout.write(f"-1\n")
