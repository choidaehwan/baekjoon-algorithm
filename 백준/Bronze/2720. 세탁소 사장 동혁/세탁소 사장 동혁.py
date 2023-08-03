import sys

T = int(sys.stdin.readline())

for _ in range(T):
    C = int(sys.stdin.readline())


    quarter = C // 25
    dime = (C % 25) // 10
    nickel = ((C % 25) % 10) // 5
    penny = ((C % 25) % 10) % 5

    print(quarter, dime, nickel, penny)