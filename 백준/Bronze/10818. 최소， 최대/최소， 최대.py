import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

print(min(line), max(line))