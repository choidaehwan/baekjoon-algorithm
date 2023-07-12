import sys

submitter = []

for _ in range(28):
    i = int(sys.stdin.readline())
    submitter.append(i)

not_subbiter = []

for j in range(1, 31):
    if j not in submitter:
        not_subbiter.append(j)

not_subbiter.sort()

for n in not_subbiter:
    print(n)