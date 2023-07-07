import sys

T = int(sys.stdin.readline())

result = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a + b)

for index, value in enumerate(result):
    case_num = index + 1
    print(f'Case #{case_num}: {value}')