n = int(input())

stack = []
index = 1
result = []
check = True

for _ in range(n):
    x = int(input())
    while index <= x:
        stack.append(index)
        result.append("+")
        index += 1
    
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        check = False
        break

if check:
    for i in result:
        print(i)
