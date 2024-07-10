import sys
input = sys.stdin.readline

def is_within_bounds(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ, |
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (2, 1)],  # ㄴ 모양들
    [(0, 0), (0, 1), (0, 2), (-1, 2)], [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)],  # ㄴㄱ 모양들
    [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (2, 0)],  # ㅜ, ㅗ 모양들
    [(0, 0), (0, 1), (-1, 1), (0, 2)], [(0, 0), (1, 0), (1, -1), (2, 0)]
]

max_sum = 0
for x in range(n):
    for y in range(m):
        for shape in shapes:
            current_sum = 0
            is_valid = True
            for dx, dy in shape:
                nx, ny = x + dx, y + dy
                if not is_within_bounds(nx, ny):
                    is_valid = False
                    break
                current_sum += graph[nx][ny]
            if is_valid:
                max_sum = max(max_sum, current_sum)

print(max_sum)
