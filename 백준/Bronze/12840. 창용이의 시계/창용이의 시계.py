import sys
input = sys.stdin.readline

def adjust_time(h, m, s, t, operation):
    # Calculate total seconds
    total_seconds = h * 3600 + m * 60 + s
    
    # Adjust seconds based on operation
    if operation == "add":
        total_seconds += t
    elif operation == "sub":
        total_seconds -= t

    # Ensure total_seconds is within a 24-hour range
    total_seconds %= 86400  # There are 86400 seconds in 24 hours

    # Calculate new h, m, s
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    
    return h, m, s

h, m, s = map(int, input().strip().split())
q = int(input().strip())

for _ in range(q):
    data = input().strip().split()
    if data[0] == "1":
        t = int(data[1])
        h, m, s = adjust_time(h, m, s, t, "add")
    elif data[0] == "2":
        t = int(data[1])
        h, m, s = adjust_time(h, m, s, t, "sub")
    elif data[0] == "3":
        sys.stdout.write(f"{h} {m} {s}\n")
