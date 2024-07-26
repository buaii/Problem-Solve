import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

k, d, a = map(int, input().strip().split("/"))
if k + a < d or d == 0:
    sys.stdout.write("hasu")
else:
    sys.stdout.write("gosu")