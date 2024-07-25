import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, k = map(int, input().strip().split())
bag = [[0, 0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    w, v = map(int, input().strip().split())
    bag.append([w, v])

for x in range(1, n+1):
    for y in range(1, k+1):
        weight = bag[x][0]
        value = bag[x][1]

        if weight <= y:
            dp[x][y] = max(dp[x-1][y-weight] + value, dp[x-1][y])
        else:
            dp[x][y] = dp[x-1][y]
print(dp[n][k])