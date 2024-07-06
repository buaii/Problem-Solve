import sys
from collections import deque
from itertools import combinations

n = int(sys.stdin.readline().strip())
shirt = list(sys.stdin.readline().strip().split())
shirts = [int(num) for num in shirt]
t, p = map(int, sys.stdin.readline().strip().split())
count = 0
for x in shirts:
	if x % t == 0:
		count += x // t
	else:
		count += x // t + 1
sys.stdout.write(f"{count}\n")
sys.stdout.write(f"{n//p} {n%p}")