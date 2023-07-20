import sys

complete_piece = [1, 1, 2, 2, 2, 8]

lack_piece = list(map(int, sys.stdin.readline().split()))

for c, l in zip(complete_piece, lack_piece):
        print(c - l, end=' ')