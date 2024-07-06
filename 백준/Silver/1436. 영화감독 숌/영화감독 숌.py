import sys
from collections import deque
from itertools import combinations
import string


n = int(sys.stdin.readline().strip())

name = '666'
count = 0
while True:
	if '666' in name:
		count += 1
		if count == n:
			break
	name = str(int(name) + 1)
sys.stdout.write(f"{name}")
	