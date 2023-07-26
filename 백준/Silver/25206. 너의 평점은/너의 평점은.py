import sys

dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
T = 20
sum = 0
num_sum = 0

for i in range(T):
    subject, number, alphabet = map(str, sys.stdin.readline().split())
    number = float(number)
    
    if alphabet == 'P':
        continue
    else:
        sum += number * dic[alphabet]
        num_sum += number

print(sum / num_sum)