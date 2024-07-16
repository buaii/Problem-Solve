import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

a, b, c = map(int, input().strip().split())

def count(a, b):
    if b == 1:
        return a%c
    else:
        if b % 2 == 0:
            temp = count(a, b//2)
            return temp * temp % c
        else:
            temp = count(a, b//2)
            return temp * temp * count(a,1) % c
sys.stdout.write(f"{count(a,b)}")

