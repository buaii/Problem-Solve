import sys
from collections import deque
input = sys.stdin.readline
import itertools

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())
p = int(input().strip())

x = a * p
if p <= c:
	y = b
else:
	y = b + (p-c)*d

print(min(x,y))