import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
import heapq

x1, y1, r1 = map(int, input().strip().split())
x2, y2, r2 = map(int, input().strip().split())

if r1 + r2 > (abs(x1-x2)**2 + abs(y1-y2)**2)**(0.5):
    print("YES")
else:
    print("NO")