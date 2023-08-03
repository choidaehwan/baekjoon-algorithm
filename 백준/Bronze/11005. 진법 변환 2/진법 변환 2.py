import sys

n, b = map(int, sys.stdin.readline().split())
rev_result = ''

while n != 0:
    a = n % b
    if a >= 10:
        rev_result += chr(a + 55)

    elif a < 10:
        rev_result += str(a)
    
    n //= b

print(rev_result[::-1])

