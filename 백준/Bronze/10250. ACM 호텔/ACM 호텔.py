t = int(input())
for _ in range(t):
	H, W, N = map(int, input().split())
	if N % H == 0:
		X = N // H
	else :
		X = N // H + 1
	if N % H == 0:
		Y = H
	else:
		Y = N % H
	if X < 10:
		print(str(Y)+"0"+str(X))
	else:
		print(str(Y)+str(X))