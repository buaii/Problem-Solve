import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

a, b = map(int, input().strip().split())

queue = deque([(a, -1)])
count = -1
check = False
while queue:
    q, count = queue.popleft()  
    if q == b:
        check = True
        break
    x = q * 2
    y = q * 10 + 1
    if x <= b:
        queue.append((x, count+1))
    if y <= b:
        queue.append((y, count+1))

if check:
    sys.stdout.write(f"{count+2}")
else:
    sys.stdout.write(f"-1")
