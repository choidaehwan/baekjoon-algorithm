import sys

N, X = map(int, sys.stdin.readline().split())
line = list(map(int, sys.stdin.readline().split()))

result = []
for i in line:
    if i < X:
        result.append(i)

for i in result:
    print(i, end = ' ')