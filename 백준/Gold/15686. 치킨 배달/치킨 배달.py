import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().strip().split()))

chicken = []
home = []
result = 1e9

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            home.append((x, y))
        elif graph[x][y] == 2:
            chicken.append((x, y))

# bruteforce
for comb in itertools.combinations(chicken, m):
    cost = 0
    for x, y in home:
        # 폐업하지 않은 치킨집과의 모든 거리 중 최솟값
        cost += min([abs(x-c[0]) + abs(y-c[1]) for c in comb])
        # 최소거리보다 비용이 커지면 계산 취소
        if cost >= result:
            break
    result = min(cost, result)

print(result)