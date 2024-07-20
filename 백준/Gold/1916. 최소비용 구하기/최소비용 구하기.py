import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().strip().split())
    graph[s].append([e, c])

start, end = map(int, input().strip().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    current_cost, current = heapq.heappop(heap)
    # 현재 비용이 더 작은 경우에만 실행
    if costs[current] < current_cost:
        continue
    for next, next_cost in graph[current]:
        sum_cost = current_cost + next_cost
        # 최종 비용이 작으면 heap에 push
        if sum_cost >= costs[next]:
            continue
        costs[next] = sum_cost
        heapq.heappush(heap, [sum_cost, next])

sys.stdout.write(f'{costs[end]}')