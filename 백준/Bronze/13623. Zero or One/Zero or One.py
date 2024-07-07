import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

data = list(map(int, input().strip().split()))
result = ['A', 'B', 'C']
count = Counter(data)

if count[0] == 1:
	sys.stdout.write(f"{result[data.index(0)]}")
elif count[1] == 1:
	sys.stdout.write(f"{result[data.index(1)]}")
else:
	sys.stdout.write("*")