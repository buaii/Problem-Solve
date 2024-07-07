import sys
from collections import deque

input = sys.stdin.readline

n = input().strip()

m = input().strip()
sys.stdout.write(f"{m[-5:-1]}{m[-1]}")