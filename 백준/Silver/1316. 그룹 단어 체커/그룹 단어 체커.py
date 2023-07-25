import sys

T = int(sys.stdin.readline())

sum = 0
for i in range(T):
    word = sys.stdin.readline().rstrip()
    only_new = [0]

    for w in word:
        if w == only_new[-1]:
            continue
        elif w not in only_new:
            only_new.append(w)
            continue
        else:
            T -= 1
            break

print(T)