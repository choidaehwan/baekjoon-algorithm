import sys

croatia_alphabet = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")

croatia_word = sys.stdin.readline().rstrip()

for a in croatia_alphabet:
    croatia_word = croatia_word.replace(a, "*")

print(len(croatia_word))