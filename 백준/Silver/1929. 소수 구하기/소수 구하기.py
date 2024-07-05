import sys

def check(m, n):
	is_prime = [True] * (n+1)
	is_prime[0] = is_prime[1] = False
	
	for i in range(2, int(n**0.5)+1, 1):
		if is_prime[i] != False:
			for num in range(i*i, n+1, i):
				is_prime[num] = False
	return is_prime

m, n = map(int, sys.stdin.readline().split())
data = check(m,n)
for i in range(m, n+1):
	if data[i] == True:
		sys.stdout.write(f"{i}\n")