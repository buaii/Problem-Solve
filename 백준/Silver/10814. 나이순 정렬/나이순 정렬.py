import sys
from collections import deque

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	age, name = map(str, sys.stdin.readline().strip().split())
	age = int(age)
	data.append((age, _, name))
data.sort()
for age, _ , name in data:
	sys.stdout.write(f"{age} {name}\n")