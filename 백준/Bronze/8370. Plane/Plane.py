import sys
from collections import deque
input = sys.stdin.readline

n, m, k, l = map(int, input().strip().split())
result = n * m + k* l
sys.stdout.write(f"{result}")
			