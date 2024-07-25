import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, m = map(int, input().strip().split())
data = [list(input().strip()) for _ in range(n)]

x_list = {}
y_list = {}

for x in range(n):
    for y in range(m):
        if data[x][y] == "X":
            x_list[x] = 1
            y_list[y] = 1

x_empty = 0
y_empty = 0

for i in range(n):
    if i not in x_list:
        x_empty += 1
for i in range(m):
    if i not in y_list:
        y_empty += 1

print(max(x_empty, y_empty))

