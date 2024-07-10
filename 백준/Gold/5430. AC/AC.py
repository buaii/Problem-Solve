import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    command = input().strip()
    n = int(input().strip())
    arr = input().strip()
    arr = arr[1:-1]
    
    if arr:
        arr = deque(arr.split(","))
    else:
        arr = deque()

    count = 0
    check = True

    for x in command:
        if x == "R":
            count += 1
        elif x == "D":
            if arr:
                if count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                sys.stdout.write("error\n")
                check = False
                break

    if check:
        if count % 2 == 1:
            arr.reverse()
        sys.stdout.write(f"[{','.join(arr)}]\n")
