import sys

N = int(sys.stdin.readline())

#for _ in range(N):
subjects = list(map(int, sys.stdin.readline().split()))
high_score = max(subjects)

total_score = 0

for s in subjects:
    fake_score = (s / high_score) * 100

    total_score += fake_score

print(total_score / N)