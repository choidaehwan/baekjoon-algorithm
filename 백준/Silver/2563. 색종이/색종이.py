import sys

matrix =[[0 for i in range(0, 101)] for _ in range(101)]

T = int(sys.stdin.readline())
sum = 0
for i in range(T):
    X, Y = map(int, sys.stdin.readline().split())

    for x in range(X, X + 10):
       for y in range(Y, Y + 10):
           if matrix[x][y] == 1:
               continue
           sum += 1
           matrix[x][y] = 1

print(sum)