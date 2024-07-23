import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

def dijkstra(start):
    costs = [1e9 for _ in range(n+1)]
    costs[start] = 0 # 자기자신은 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_cost > costs[current_node]:
            continue
        for next_node, next_cost in graph[current_node]:
            sum_cost = current_cost + next_cost
            if sum_cost < costs[next_node]:
                costs[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return costs

n, e = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]


for _ in range(e):
    u, v, w = map(int, input().strip().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

v1, v2 = map(int, input().strip().split())

# v1과 v2를 거쳐야 하므로 각 지점에서 다익스트라 수행
costs_original = dijkstra(1)
costs_v1 = dijkstra(v1)
costs_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> n
first_case = costs_original[v1] + costs_v1[v2] + costs_v2[n]
# 1 -> v2 -> v1 -> n
second_case = costs_original[v2] + costs_v2[v1] + costs_v1[n]

result = min(first_case, second_case)

if result > 1e8:
    sys.stdout.write("-1")
else:
    sys.stdout.write(f"{result}")

