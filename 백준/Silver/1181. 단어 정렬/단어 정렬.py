import sys
from collections import deque

n = int(sys.stdin.readline().strip())

data = []

for _ in range(n):
	word = sys.stdin.readline().strip()
	if word not in data:
		data.append(word)
data.sort()
data.sort(key=lambda x: len(x))
for word in data:
	sys.stdout.write(f"{word}\n")