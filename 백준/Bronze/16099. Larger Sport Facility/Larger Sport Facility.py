import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

t = int(input().strip())
for _ in range(t):
    l1, w1, l2, w2 = map(int, input().strip().split())

    if l1 * w1 > l2 * w2:
        sys.stdout.write("TelecomParisTech\n")
    elif l1 * w1 < l2 * w2:
        sys.stdout.write("Eurecom\n")
    else:
        sys.stdout.write("Tie\n")