import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n = int(input())
data = [[] for _ in range(n)]
result = []

for i in range(n):
    data[i].append(input().strip())

for i in range(len(data[0][0])):
    for x in range(1, len(data)):
        if data[0][0][i] != data[x][0][i]:
            result.append("?")        
            break
    if i == len(result):
        result.append(data[0][0][i])
        
for x in result:
    print(x, end="")