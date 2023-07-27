import sys

n, m = map(int, sys.stdin.readline().split())

list_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
list_b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        list_a[i][j] += list_b[i][j]
        
for line in list_a:
    print(*line)