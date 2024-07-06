import sys
from collections import deque
from itertools import combinations

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()
k = sys.stdin.readline().strip()
x = 0
if n.isdigit():
	x = int(n) + 3
elif m.isdigit():
	x = int(m) + 2
elif k.isdigit():
	x = int(k) + 1

if x % 3 == 0 and x % 5 == 0:
	sys.stdout.write("FizzBuzz\n")
elif x % 3 == 0 and x % 5 != 0:
	sys.stdout.write("Fizz\n")
elif x % 3 != 0 and x % 5 == 0:
	sys.stdout.write("Buzz\n")
else:
	sys.stdout.write(f"{x}\n")