def check(s):
	pre = False
	ans = 0
	count = 0
	for i in s:
		if not pre:
			if i == "O":
				pre = True
				count += 1
				ans += count
		else:
			if i == "O":
				count += 1
				ans += count
			else:
				count = 0
	return ans

n = int(input())
for _ in range(n):
	print(check(input()))
		