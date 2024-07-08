import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().strip().split())

# 블록 높이 입력 받기
graph = []
for _ in range(n):
    graph.extend(map(int, input().rstrip().split()))

# 높이별 블록 수 계산
height_counts = Counter(graph)

min_height = min(height_counts)
max_height = max(height_counts)

time = sys.maxsize
result = 0

for height in range(min_height, max_height + 1):
    use_block = 0
    get_block = 0
    for current_height, count in height_counts.items():
        if current_height > height:
            get_block += (current_height - height) * count
        else:
            use_block += (height - current_height) * count

    if use_block > get_block + b:
        continue

    count = get_block * 2 + use_block
    if count <= time:
        time = count
        result = height

sys.stdout.write(f"{time} {result}\n")
