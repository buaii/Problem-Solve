import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

def pre_order(x):
    visited[x] = True
    y, z = graph[x]

    sys.stdout.write(f"{x}")
    
    if y != "." and not visited[y]:
        pre_order(y)
        
    if z != "." and not visited[z]:
        pre_order(z)

def in_order(x):
    visited[x] = True
    y, z = graph[x]

    if y != "." and not visited[y]:
        in_order(y)

    sys.stdout.write(f"{x}")

    if z != "." and not visited[z]:
        in_order(z)

def post_order(x):
    visited[x] = True
    y, z = graph[x]

    if y != "." and not visited[y]:
        post_order(y)

    if z != "." and not visited[z]:
        post_order(z)

    sys.stdout.write(f"{x}")

n = int(input().strip())
graph = {}
data = []
for _ in range(n):
    x, y, z = map(str, input().strip().split())
    data.append(x)
    graph[x] = [y, z]

visited = {}
for d in data:
    visited[d] = False
pre_order("A")
sys.stdout.write("\n")

visited = {}
for d in data:
    visited[d] = False
in_order("A")
sys.stdout.write("\n")

visited = {}
for d in data:
    visited[d] = False
post_order("A")
sys.stdout.write("\n")