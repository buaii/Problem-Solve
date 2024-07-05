import sys
from collections import deque
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

dp = [0] * (n+1)
stair = [0]
result = 0
for i in range(n):
	stair.append(int(sys.stdin.readline().rstrip()))

if n == 1:
	dp[1] = stair[1]
	sys.stdout.write(f"{dp[n]}")	
elif n == 2:
	dp[1] = stair[1]
	dp[2] = stair[1] + stair[2]	
	sys.stdout.write(f"{dp[n]}")	
else:
	dp[1] = stair[1]
	dp[2] = stair[1] + stair[2]
	dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

	for i in range(4, n+1):
		dp[i] = max(dp[i-3]+stair[i-1]+stair[i], stair[i]+dp[i-2])

	sys.stdout.write(f"{dp[n]}")