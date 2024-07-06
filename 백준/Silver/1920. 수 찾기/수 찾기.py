import sys
from collections import deque

n = int(sys.stdin.readline().strip())
data = []

input_data = sys.stdin.readline().strip().split()
input_data.sort()	
m = int(sys.stdin.readline().strip())

check_data = sys.stdin.readline().strip().split()

for x in check_data:
	start = 0
	end = n -1
	found = 0
	while start <= end:
		mid = (start+end) // 2
		if input_data[mid] == x:
			found = 1
			break
		elif input_data[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	sys.stdout.write(f"{found}\n")