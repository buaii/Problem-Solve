def isPrime(s):
	if s == 1:
		return False
	for i in range(2, s):
		if s % i == 0:
			return False
	return True

n = int(input())
data = list(map(int, input().split()))
result = 0

for s in data:
	if isPrime(s):
		result += 1
	
print(result)