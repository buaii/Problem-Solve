import sys
from collections import deque
from itertools import combinations
import string

input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().strip().split()))

arr = sorted(set(data))

dic = {arr[i]:i for i in range(len(arr))}

for i in data:
	print(dic[i], end=" ")
