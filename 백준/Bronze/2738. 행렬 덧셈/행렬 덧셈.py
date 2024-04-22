n, m = map(int, input().split())
N = []
M = []
for _ in range(n):
	N.append(list(map(int, input().split())))
for _ in range(n):
	M.append(list(map(int, input().split())))

ans = []
for i, j in zip(N,M):
	temp = []
	for k in range(m):
		temp.append(i[k]+j[k])
	ans.append(temp)
for r in ans:
	print(*r)