import sys
from collections import deque

m = int(sys.stdin.readline().rstrip())
data = {}
for _ in range(m):
	
	command_line = list(map(str, sys.stdin.readline().rstrip().split()))
	if len(command_line) == 1:
		command = command_line[0]
	else:
		command, x = command_line[0], command_line[1]
		x = int(x)
	if command == "add":
		if x not in data:
			data[x] = x	
	elif command == "remove":
		if x in data:
			del data[x]
	elif command == "check":
		if x in data:
			sys.stdout.write("1\n")
		else:
			sys.stdout.write("0\n")
	elif command == "toggle":
		if x in data:
			del data[x]
		else:
			data[x] = x
	elif command == "all":
		data = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20}
	elif command == "empty":
		data = {}