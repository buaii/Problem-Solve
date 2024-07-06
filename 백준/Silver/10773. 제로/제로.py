import sys
from collections import deque
from itertools import combinations
import string

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	command = int(sys.stdin.readline().strip())
	if not command:
		data.pop()
	else:
		data.append(command)
	
sys.stdout.write(f"{sum(data)}")