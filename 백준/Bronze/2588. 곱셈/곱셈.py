import sys 

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline())

b_hundred = b % 1000 // 100
b_ten = b % 100 // 10
b_one = b % 10 // 1


print(a * b_one)
print(a * b_ten)
print(a * b_hundred)
print(a * b)
