import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
	n = int(input().strip())
	dp = [0] * 100
	dp[0] = 1
	dp[1] = 1
	dp[2] = 1
	dp[3] = 2
	dp[4] = 2
	for i in range(5, n):
		dp[i] = dp[i-5] + dp[i-1]
	sys.stdout.write(f"{dp[n-1]}\n")

	