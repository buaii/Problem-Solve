def isPel(n):
    return str(n) == str(n)[::-1]

n = int(input())
while n != 0:
	if isPel(n):
		print('yes')
	else:
		print('no')
	n = int(input())