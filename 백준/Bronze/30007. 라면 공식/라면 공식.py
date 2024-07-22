import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n = int(input().strip())
for _ in range(n):
    a, b, x = map(int, input().strip().split())

    w = a*(x - 1) + b

    sys.stdout.write(f"{w}\n")