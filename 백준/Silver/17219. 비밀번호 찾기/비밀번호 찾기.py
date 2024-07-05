import sys
from collections import deque
from collections import defaultdict

n, m = map(int, sys.stdin.readline().rstrip().split())
data = defaultdict()
for _ in range(n):
	site, pw = map(str, sys.stdin.readline().rstrip().split())
	data[site] = pw
for _ in range(m):
	myFind = sys.stdin.readline().rstrip()
	sys.stdout.write(f"{data[myFind]}\n")