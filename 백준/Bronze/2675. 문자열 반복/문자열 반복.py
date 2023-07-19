import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(str, sys.stdin.readline().rstrip().split())

    for i in b:
        print(int(a) * i, end ='')
    print()