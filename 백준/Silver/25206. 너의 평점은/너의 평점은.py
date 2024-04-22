score = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
ans = 0
total_time = 0
for _ in range(20):
	n, h, s = map(str, input().split())
	if s == "P":
#		total_time += float(h)
		continue
	total_time += float(h)
	ans = ans + float(h)*score[s]
	
print(round((ans/total_time), 6))