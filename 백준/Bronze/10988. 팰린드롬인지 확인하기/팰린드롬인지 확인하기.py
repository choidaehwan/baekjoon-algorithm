import sys

word = list(map(str, sys.stdin.readline().rstrip()))

i = 0
while i < (len(word) // 2):
    if word[i] == word[len(word) - 1- i]:
        i += 1
    else:
        print(0)
        break

if i == (len(word) // 2):
    print(1)