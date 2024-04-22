import string 
s = input()
ans = ''
for i in s:
	if i in string.ascii_lowercase:
		ans += ''.join(i.upper())
	else:
		ans += ''.join(i.lower())		
print(ans)
