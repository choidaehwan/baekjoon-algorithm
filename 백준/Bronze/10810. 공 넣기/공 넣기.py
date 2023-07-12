import sys

# N = 바구니 갯수, 번호 | M = 공을 넣으려는 횟수
N, M = map(int, sys.stdin.readline().split())
# i ~ j 까지가 바구니 범위 | k = 공 번호

bucket_list = [0 for _ in range(N)]

for i in range(M):
    i, j, k = map(int, sys.stdin.readline().split())

    for index in range(i - 1, j):
        bucket_list[index] = k

for b in bucket_list:
    if b == bucket_list[-1]:
        print(b)
    else:
        print(b, end=' ')