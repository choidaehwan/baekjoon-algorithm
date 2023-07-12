import sys

all_student = [i for i in range(1, 31)]

for _ in range(28):
    subbmitter = int(sys.stdin.readline())
    all_student.remove(subbmitter)

print(min(all_student))
print(max(all_student))