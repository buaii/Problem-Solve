n = int(input())
myList = []
for _ in range(n):
	for a in input().split():
		myList.append(a)
	myNum = 0
	for x in myList:
		if x == "@":			
			myNum *= 3
		elif x == "%":
			myNum += 5
		elif x == "#":
			myNum -= 7
		else:
			myNum = float(x)
	print(f"{myNum:.2f}")