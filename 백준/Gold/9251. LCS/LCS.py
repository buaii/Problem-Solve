import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
import heapq

data1 = list(input().strip())
data2 = list(input().strip())

dp = [[0] * (len(data2)+1) for _ in range(len(data1)+1)]

for i in range(1, len(data1)+1):
    for j in range(1, len(data2)+1):
        if data1[i-1] == data2[j-1]: 
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(data1)][len(data2)])
