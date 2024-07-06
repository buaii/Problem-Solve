import sys
from collections import deque
from itertools import combinations

n = float(sys.stdin.readline().strip())
data = [int(sys.stdin.readline().strip()) for _ in range(int(n))]
data.sort()


if len(data) == 0:
	sys.stdout.write("0")
else:
	ex = (n * 0.15)
	if ex % 1 >= 0.5:
		ex = int(ex // 1 + 1)
	else:
		ex = int(ex // 1)
	data = data[ex:len(data)-ex]
	avg = sum(data) / len(data)
	
	if avg % 1 >= 0.5:
		avg = int(avg // 1 + 1)
	else:
		avg = int(avg // 1)
	sys.stdout.write(f"{avg}")
