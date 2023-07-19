import sys

word = sys.stdin.readline()

count = 0

for w in word:
    if w in 'ABC':
        count += 3

    elif w in 'DEF':
        count += 4

    elif w in 'GHI':
        count += 5

    elif w in 'JKL':
        count += 6

    elif w in 'MNO':
        count += 7

    elif w in 'PQRS':
        count += 8

    elif w in 'TUV':
        count += 9

    elif w in 'WXYZ':
        count += 10

print(count)