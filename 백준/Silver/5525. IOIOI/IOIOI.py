import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
p = "IOI"
pn = p + "OI"*(n-1)

data = list(input().strip())
count = 0
for i in range(len(data)-2):
	check = data[i:i+2+2*(n-1)+1]
	test = ''.join([char for char in check])
	
	if  test == pn:
		count += 1
sys.stdout.write(f"{count}")