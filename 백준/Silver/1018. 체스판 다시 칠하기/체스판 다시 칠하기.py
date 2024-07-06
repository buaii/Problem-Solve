import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

board = []
for _ in range(n):
	board.append(list(sys.stdin.readline().strip()))
count = []

for i in range(n-7):
	for j in range(m-7):
		index_w = 0
		index_b = 0
		for k in range(i, i+8):
			for l in range(j, j+8):
				if (k+l) % 2 == 0:
					if board[k][l] == "W":
						index_w += 1
					if board[k][l] == "B":
						index_b += 1
				else:
					if board[k][l] == "B":
						index_w += 1
					if board[k][l] == "W":
						index_b += 1
		count.append(min(index_w, index_b))
sys.stdout.write(f"{min(count)}")	