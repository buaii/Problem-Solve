import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())
data = list(map(int, input().strip().split()))

dp = [1] * (n+1)

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
sys.stdout.write(f"{max(dp)}")