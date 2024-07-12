import sys
from collections import deque
input = sys.stdin.readline
import itertools

n, m = map(int, input().strip().split())

data = list(input().strip().split())

for x in data:
	x = int(x)
	result = x*100 // n
	if 0 <= result <= 4:
		print(1, end=" ")
	elif 4 < result <= 11:
		print(2, end=" ")
	elif 11 < result <= 23:
		print(3, end=" ")
	elif 23 < result <= 40:
		print(4, end=" ")
	elif 40 < result <= 60:
		print(5, end=" ")
	elif 60 < result <= 77:
		print(6, end=" ")
	elif 77 < result <= 89:
		print(7, end=" ")
	elif 89 < result <= 96:
		print(8, end=" ")
	elif 96 < result <= 100:
		print(9, end=" ")