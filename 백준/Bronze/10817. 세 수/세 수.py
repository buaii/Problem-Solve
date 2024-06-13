myList = []
a, b, c = map(int, input().split())
myList.append(a)
myList.append(b)
myList.append(c)
myList.sort()
print(myList[-2])
