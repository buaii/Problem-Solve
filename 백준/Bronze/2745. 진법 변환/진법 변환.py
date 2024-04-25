N, b = map(str, input().split())
s_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
for i,s in enumerate(reversed(N)):
	 ans += int(b)**i * s_list.index(s)
print(ans)