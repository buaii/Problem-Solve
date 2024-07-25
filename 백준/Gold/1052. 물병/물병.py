import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, k = map(int, input().strip().split())
ans = 0
while bin(n).count('1') > k:
    ans += 1
    n += 1
print(ans)