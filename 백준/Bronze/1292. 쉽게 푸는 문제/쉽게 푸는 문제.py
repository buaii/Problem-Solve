import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, m = map(int, input().strip().split())
arr = []
idx = 1

while len(arr) < 1000:
    for i in range(idx):
        arr.append(idx)
    idx += 1

print(sum(arr[n-1:m]))

