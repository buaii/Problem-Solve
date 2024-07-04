n = int(input())

result = []
for _ in range(n):
	data = list(map(int, input().split()))
	result.append(data)
result.sort(key=lambda x: [x[1],x[0]])
for item in result:
	print(*item)
