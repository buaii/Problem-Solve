from collections import Counter
import sys

n = int(input())

data = []
for _ in range(n):
	data.append(int(sys.stdin.readline()))

avg = sum(data) / len(data)
data.sort()
mid = data[len(data)//2]

counter = Counter(data)
frequency = 0
max_counter = max(counter.values())
most_elements = [key for key, value in counter.items() if value == max_counter]
most_elements.sort()

if len(most_elements) > 1:
	frequency = most_elements[1]
else:
	frequency = most_elements[0]

width = max(data) - min(data)

print(round(avg))
print(mid)
print(frequency)
print(width)