import sys

T = int(sys.stdin.readline())

sum = T

for _ in range(T):
    word = sys.stdin.readline().rstrip()

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            sum -= 1
            break

print(sum)