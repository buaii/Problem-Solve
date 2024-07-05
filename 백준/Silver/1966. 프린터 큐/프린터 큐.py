import sys
from collections import deque

s = int(sys.stdin.readline())

for _ in range(s):
	queue = deque()
	n, m = map(int, sys.stdin.readline().split())
	doc = list(map(int, sys.stdin.readline().split()))
	# id 부여
	id = 0
	for item in doc:
		queue.append((item, id))
		id += 1
	# m번째 문서의 id 확인
	_, check_id = queue[m]
	# 출력 
	count = 0
	while True:
		queue_importance = max(item[0] for item in queue)
		importance, check = queue.popleft()

		if importance == queue_importance:
			count += 1
			if check == check_id:
				print(count)
				break
		elif importance != queue_importance:
			queue.append((importance, check))

	