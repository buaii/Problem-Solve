import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

def bfs(n):
    if n == 0:
        queue = deque([1])
    else:
        queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == m:
            return visited[x]
        for dx in (x-1, x+1, 2*x):
            if 0 <= dx <= 100000 and not visited[dx]:
                if dx == 2*x:
                    visited[dx] = visited[x]
                    queue.appendleft(dx)
                else:
                    visited[dx] = visited[x] + 1
                    queue.append(dx)

n, m = map(int, input().strip().split())
visited = [0] * 100001
if n == 0:
    if m == 0:
        sys.stdout.write("0")
    else:
        sys.stdout.write(f"{bfs(n)+1}")
else:
    sys.stdout.write(f"{bfs(n)}")
