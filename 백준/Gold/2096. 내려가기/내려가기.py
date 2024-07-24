import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n = int(input())
data = list(map(int, input().strip().split()))

max_dp = [data[:] for _ in range(2)]
min_dp = [data[:] for _ in range(2)]

for _ in range(n-1):
    data = list(map(int, input().strip().split()))
    for y in range(3):
        if y == 0:
            max_dp[1][y] = max(max_dp[0][0], max_dp[0][1]) + data[y]
        elif y == 1:
            max_dp[1][y] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + data[y]
        else:
            max_dp[1][y] = max(max_dp[0][1], max_dp[0][2]) + data[y]
    max_dp[0] = max_dp[1][:]    
    for y in range(3):
        if y == 0:
            min_dp[1][y] = min(min_dp[0][0], min_dp[0][1]) + data[y]
        elif y == 1:
            min_dp[1][y] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + data[y]
        else:
            min_dp[1][y] = min(min_dp[0][1], min_dp[0][2]) + data[y]
    min_dp[0] = min_dp[1][:]

print(max(max_dp[1]))
print(min(min_dp[1]))
                