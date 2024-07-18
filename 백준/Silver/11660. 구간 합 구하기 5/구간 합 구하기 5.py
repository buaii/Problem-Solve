import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
# 누적 합 적용
for y in range(n):
    for x in range(n):
        if 0 <= y-1 < n:
            data[x][y] += data[x][y-1]
        if 0 <= x-1 < n:
            data[x][y] += data[x-1][y]
        if 0 <= x-1 < n and 0 <= y-1 < n:
            data[x][y] -= data[x-1][y-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    result = 0
    # index 정렬
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    # 누적합 계산
    result = data[x2][y2] 
    if 0 <= y1-1 < n:
        result -= data[x2][y1-1]
    if 0 <= x1-1 < n:
        result -= data[x1-1][y2]
    if 0 <= y1-1 < n and 0 <= x1-1 < n:
        result += data[x1-1][y1-1]
    sys.stdout.write(f"{result}\n")