import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

v, l = map(int, input().strip().split())
start = int(input().strip())
graph = [[] for _ in range(v+1)]

for _ in range(l):
    st, ed, w = map(int, input().strip().split())
    graph[st].append([ed, w])

costs = [1e9 for _ in range(v+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    current_cost, current_node = heapq.heappop(heap)
    # 갱신이 불가능하면 패스
    if current_cost > costs[current_node]:
        continue
    for next_node, next_cost in graph[current_node]:
        sum_cost = current_cost + next_cost
        # 다음 노드까지 최소비용보다 크면 패스
        if sum_cost < costs[next_node]:
            costs[next_node] = sum_cost
            heapq.heappush(heap, [sum_cost, next_node])
        

for i in range(1, len(costs)):
    if costs[i] == 1e9:
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(f"{costs[i]}\n")