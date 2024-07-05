import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
man = list(map(int, sys.stdin.readline().rstrip().split()))
man.sort()
result = []
mysum = 0
for m in man:
	mysum += m
	result.append(mysum)
sys.stdout.write(f"{sum(result)}")