import sys

N, B = map(int, sys.stdin.readline().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rev_base = ''
while N > 0:
    N, mod = divmod(N, B)
    rev_base += str(arr[mod])

print(rev_base[::-1])
