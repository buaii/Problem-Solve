import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
	k = int(sys.stdin.readline().rstrip())
	
	dp = [0] * 11
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	dp[4] = 7
	for i in range(5, k+1):
		dp[i] = dp[i-2] + dp[i-1] + dp[i-3]
	sys.stdout.write(f"{dp[k]}\n")