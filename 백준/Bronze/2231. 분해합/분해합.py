s = int(input())

result = 0
Answer = []
for n in range(1, s):
	result += n
	answer = n
	while n > 0:
		number = n % 10
		result += number
		n = n // 10
	if result == s:
		Answer.append(answer)
		break
	result = 0

if len(Answer) == 0:
	print(0)
else:
	print(Answer[0])
	