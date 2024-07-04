N = int(input())
apart = []
for _ in range(N):
	k = int(input())
	n = int(input())
	sum = 0
	for j in range(k+1):
		floor = []
		for i in range(1,n+1):
			if len(apart) == 0:
				floor.append(i)
			else:
				for x in apart[j-1][:i]:
					sum += x
				floor.append(sum)
				sum = 0
		apart.append(floor)
		floor = []
	print(apart[k][n-1])
	apart = []