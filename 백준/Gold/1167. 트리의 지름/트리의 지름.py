import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

def dfs(start, dist, visited):
    visited[start] = True
    max_dist = dist
    far_node = start

    for next, d in graph[start]:
        if not visited[next]:
            visited[next] = True
            next_node, next_dist = dfs(next, dist+d, visited)
            if next_dist > max_dist:
                far_node = next_node
                max_dist = next_dist

    return far_node, max_dist

v = int(input().strip())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, input().strip().split()))
    for i in range(1, len(data)-1, 2):
        graph[data[0]].append([data[i], data[i+1]])
        
# 가장 깊은 노드 찾기
visited = [False] * (v+1)
node, dist = dfs(1, 0, visited)
# 트리 지름 찾기
visited = [False] * (v+1)
node, dist = dfs(node, 0, visited)
sys.stdout.write(f"{dist}")