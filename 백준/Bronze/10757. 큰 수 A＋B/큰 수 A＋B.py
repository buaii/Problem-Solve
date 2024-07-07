import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
sys.stdout.write(f"{n+m}")