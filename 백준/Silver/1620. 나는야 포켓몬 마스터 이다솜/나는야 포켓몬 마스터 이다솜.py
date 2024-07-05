import sys

n, m = map(int, sys.stdin.readline().split())
pocket_int = {}
pocket_str = {}
for i in range(1, n+1):
	name = sys.stdin.readline().rstrip("\n")
	pocket_int[i] = name
	pocket_str[name] = i

for i in range(m):
	quiz = sys.stdin.readline().rstrip("\n")
	if quiz.isnumeric():
		sys.stdout.write(f"{pocket_int[int(quiz)]}\n")
	else:
		sys.stdout.write(f"{pocket_str[quiz]}\n")