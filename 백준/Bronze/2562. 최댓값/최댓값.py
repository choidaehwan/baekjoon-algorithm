import sys

list = []
for i in range(9):
    a = int(sys.stdin.readline())
    list.append(a)

print(max(list))
print(list.index(max(list)) + 1)