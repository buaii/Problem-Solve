import sys
from itertools import permutations
input = sys.stdin.readline

# 입력
n, m = map(int, input().strip().split())
result = list(map(int, input().strip().split()))
result.sort()

# 순열 생성
s = set(permutations(result, m))

# 출력
for x in s:
    print(' '.join(map(str, x)))
