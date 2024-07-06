import sys
from collections import deque
from itertools import combinations
import string

n = int(sys.stdin.readline().strip())
data = list(sys.stdin.readline().strip())
sum = 0
for idx, x in enumerate(data):
	i = string.ascii_lowercase.index(x)
	h = (i+1) * (31**idx) 
	sum += h
sum = sum % 1234567891
sys.stdout.write(f"{sum}")