import sys

list_a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_value = 0
max_line = 0
for i in range(len(list_a)):
    if max_value < max(list_a[i]):
        max_value = max(list_a[i])
        max_line = i

print(max_value)
print(max_line + 1, list_a[max_line].index(max_value) + 1)