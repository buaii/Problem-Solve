import sys
input = sys.stdin.readline

n, m, b = map(int, input().strip().split())

graph = []
min_height = 256
max_height = 0
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().rstrip().split()]
    graph.append(row)
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))

# 높이별 블록 수를 미리 계산
height_counts = [0] * 257
for row in graph:
    for height in row:
        height_counts[height] += 1

time = sys.maxsize
result = 0

for height in range(min_height, max_height + 1):
    use_block = 0
    get_block = 0
    for current_height in range(257):
        if current_height > height:
            get_block += (current_height - height) * height_counts[current_height]
        else:
            use_block += (height - current_height) * height_counts[current_height]

    if use_block > get_block + b:
        continue

    count = get_block * 2 + use_block
    if count <= time:
        time = count
        result = height

sys.stdout.write(f"{time} {result}")
