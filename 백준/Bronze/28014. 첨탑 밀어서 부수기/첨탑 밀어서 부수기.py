import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().strip().split()))
visited = [0] * (n+1)
count = 0

for i in range(n):
	if not visited[i]:
		count += 1
		visited[i] = 1
		for j in range(i, n-1):	
			if data[j] > data[j+1]:
				visited[j+1] = 1
			else:
				break

sys.stdout.write(f"{count}")