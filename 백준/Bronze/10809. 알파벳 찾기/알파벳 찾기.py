import sys

S = sys.stdin.readline().rstrip()

alphabet = [chr(i) for i in range(97, 123)]
alphabet_count = [-1 for n in range(26)]
avoid_duplication = []

for i, s in enumerate(S):
    if s not in avoid_duplication and s in alphabet:
        avoid_duplication.append(s)
        order = ord(s) - 97
        alphabet_count[order] = i

for i in alphabet_count:
    print(i, end = ' ')
