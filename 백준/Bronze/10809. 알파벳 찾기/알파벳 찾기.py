import sys

S = sys.stdin.readline().rstrip()
alphabet = [chr(i) for i in range(97, 123)]

for a in alphabet:
    if a in S:
        print(S.index(a), end = ' ')
    else:
        print(-1, end= ' ')