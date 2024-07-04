data = list(map(int, input().split()))
data.sort()

area = data[0] * data[1]
Area = data[0] * data[1]
a = data[1]
b = data[0]
while True:
	area -= (b*b) * (a//b)
	if area == 0:
		break
	a, b = b, a%b
		
print(b)
print(Area//b)