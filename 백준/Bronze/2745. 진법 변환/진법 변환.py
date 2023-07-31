import sys
import math

N, B = map(str, sys.stdin.readline().split())

def change(num):
    if ord("A") <= ord(num) <= ord("Z"):
        return ord(num) - ord("A") + 10
    else:
        return int(num)

sum = 0
i = 0
for n in N[::-1]:
    sum += change(n) * math.pow(int(B), i)
    i += 1

print(int(sum))
