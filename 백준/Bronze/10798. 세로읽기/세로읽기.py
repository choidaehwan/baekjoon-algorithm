import sys

table = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]

for i in range(5):
    lack = 15 - len(table[i])
    for _ in range(lack):
        table[i].append('*')

result = ''
for i in range(15):
    for j in range(5):
        if table[j][i] == '*': 
            pass
        else:
            result += table[j][i]

print(result)