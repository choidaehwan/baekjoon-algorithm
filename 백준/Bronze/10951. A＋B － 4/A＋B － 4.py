import sys

result = []

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())

        result.append(a + b)
    except:
        for i in result:
            print(i)
        break