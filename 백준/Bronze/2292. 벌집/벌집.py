n = int(input())

if n == 1:
	print(1)
else:
	result = 1
	count = 1
	index = 2
	while True:
		if result + (index-1)*6 >= n:
			print(count+1)
			break
		else:
			result += (index-1)*6
			count += 1
			index += 1