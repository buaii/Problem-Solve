import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())

if n % 5 == 0:
    print(n//5)
else:
    print(n//5+1)