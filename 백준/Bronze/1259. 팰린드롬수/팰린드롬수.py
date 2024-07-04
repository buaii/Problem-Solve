def isfel(s):
	if len(s) <= 1:
		return True
	else:
		if s[0] == s[-1]:
			return isfel(s[1:-1])
		else:
			return False

s = input()
while s != "0":
	if isfel(s):
		print("yes")
	else:
		print("no")

	s = input()