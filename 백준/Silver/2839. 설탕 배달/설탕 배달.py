n = int(input())

max = n // 5
result = False
for s in range(max, -1, -1):
	remain = n - s*5
	if remain % 3 == 0:
		print(s+remain//3)
		result = True
		break
if not result:
	print(-1)