import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools
import heapq

w, h = map(int, input().strip().split())

sys.stdout.write(f"{w*h/2}")