import sys
from collections import deque

n = int(sys.stdin.readline().strip())
data = deque()

for i in range(1,n+1):
	data.append(i)
while len(data) != 1:
	data.popleft()
	x = data.popleft()
	data.append(x)

sys.stdout.write(f"{data.popleft()}")