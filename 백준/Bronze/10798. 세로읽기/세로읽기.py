import sys

table = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]

result = ''
for i in range(15):
    for j in range(5):
        if len(table[j]) <= i:
            pass
        else:
            result += table[j][i]

print(result)