def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

N = int(input().strip())

if N == 1:
    exit()

result = prime_factors(N)

for factor in result:
    print(factor)
