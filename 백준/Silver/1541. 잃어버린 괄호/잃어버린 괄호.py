import sys
input = sys.stdin.readline

data = list(map(str, input().strip().split("-")))
result = []
for i in data:
	result.append(list(map(int, i.split("+"))))
for idx, x in enumerate(result):
	result[idx] = sum(x)
sum = result[0]
for i in result[1:]:
	sum -= i
sys.stdout.write(f"{sum}")