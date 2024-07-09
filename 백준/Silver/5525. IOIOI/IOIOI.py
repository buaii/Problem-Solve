import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

data = input().strip()

cursor = 0
result = 0
count = 0
while cursor < m-1:
#	print(count, cursor, result)
#	print(data[cursor:cursor+3])
	if data[cursor:cursor+3] == "IOI":
		count += 1
		cursor += 2
		if count == n:
			count -= 1
			result += 1
	else:
		cursor += 1
		count = 0
sys.stdout.write(f"{result}")