import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())

data = list(map(int, input().strip().split()))
data2 = [0 for _ in range(n+2)]
for idx, d in enumerate(data):
    data2[idx+1] = d

dp = [0] * (n*3)

for i in range(1, n+1):
    dp[i] = max(dp[i], data2[i])
    for j in range(1, i+1):
        dp[i+j] = max(dp[i+j], dp[i] + data2[j])

print(dp[n])