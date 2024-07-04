n = int(input())
data = 1
while n != 0:
	data *= n
	n -= 1
result = 0
for i in reversed(str(data)):
	if i != "0":
		break
	else:
		result += 1	
print(result)