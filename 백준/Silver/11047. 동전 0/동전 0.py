import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
value_list = []
for _ in range(n):
	value = sys.stdin.readline().rstrip()
	value_list.append(value)
count = 0
m = int(m)
for value in reversed(value_list):
	value = int(value)
	if m % value != m:
		count += m // value
		m = m % value

sys.stdout.write(f"{count}")
	