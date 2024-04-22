s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = input()
length = max(len(s1),len(s2),len(s3),len(s4),len(s5))
ans = ''

for i in range(length):
	if i < len(s1):
		ans = ans + ''.join(s1[i])
	if i < len(s2):
		ans = ans + ''.join(s2[i])
	if i < len(s3):
		ans = ans + ''.join(s3[i])
	if i < len(s4):
		ans = ans + ''.join(s4[i])
	if i < len(s5):
		ans = ans + ''.join(s5[i])
print(ans)
