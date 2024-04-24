ans = -1
r, c = 0, 0
for i in range(9):
	input_list = list(map(int, input().split()))
	for j, n in enumerate(input_list):
		if ans < n:
			ans = n
			r = i+1
			c = j+1
print(ans)	
print(r,c)