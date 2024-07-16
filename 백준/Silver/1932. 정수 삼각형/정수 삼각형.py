import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())

data = [list(map(int, input().strip().split())) for _ in range(n)]
# 다이나믹 프로그래밍을 위한 뒤집기
data.reverse()

for idx, d in enumerate(data):
    if idx == 0:
        continue
    for i, x in enumerate(d):
        data[idx][i] = max(x+data[idx-1][i], x+data[idx-1][i+1])
print(*data[n-1])
