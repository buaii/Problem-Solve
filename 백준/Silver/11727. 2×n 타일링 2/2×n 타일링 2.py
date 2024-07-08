import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5

#1 1
#2 3
#3 5
#4 11

for i in range(4, n+1):
	dp[i] = dp[1] * dp[i - 1] + (dp[2]-1) * dp[i - 2]
sys.stdout.write(f"{dp[n]%10007}")