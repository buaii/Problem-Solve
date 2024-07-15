import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

result = []

for i in range(len(A)):
    if A[i] > B[i]:
            result.append("A")
    elif A[i] == B[i]:
            result.append("D")
    else:
            result.append("B")

count = Counter(result)
if count['A'] > count['B']:
    sys.stdout.write("A\n")
elif count['A'] < count['B']:
    sys.stdout.write("B\n")
else:
    sys.stdout.write("D\n")