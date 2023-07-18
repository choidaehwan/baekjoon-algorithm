import sys

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline().rstrip()

    print(S[0], end='')
    print(S[-1])