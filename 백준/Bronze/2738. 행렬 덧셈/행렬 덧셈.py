import sys

i, j = map(int, sys.stdin.readline().split())

list_a = []
list_b = []
list_ab = [0 for _ in range(i * j)]

for _ in range(i):
    list_a += list(map(int, sys.stdin.readline().split()))

for _ in range(i):
    list_b += list(map(int, sys.stdin.readline().split()))

for index in range(i * j):
    list_ab[index] = list_a[index] + list_b[index]

for line in range(i):
    for ab in list_ab[0 + (j * line):j + (j * line)]:
        print(ab, end=' ')
    print()