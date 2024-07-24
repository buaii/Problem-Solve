import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, m = map(int, input().strip().split())

for _ in range(n):
    data = list(input().strip())
    for i in data[::-1]:
        print(i, end="")

    print()