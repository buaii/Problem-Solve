import sys
from collections import deque
from collections import defaultdict


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    cloth = defaultdict(list)     
    for _ in range(m):
        item, type_ = sys.stdin.readline().rstrip().split()
        cloth[type_].append(item)
    
    count = 1
    for type_ in cloth:
        count *= (len(cloth[type_]) + 1)      
    sys.stdout.write(f"{count - 1}\n")  