import sys
from collections import deque
from itertools import combinations
import string


a, b, v = map(int, sys.stdin.readline().strip().split())

if (v - b) % (a - b) == 0:
	sys.stdout.write(f"{(v-b)//(a-b)}")
else:
	sys.stdout.write(f"{(v-b)//(a-b)+1}")	