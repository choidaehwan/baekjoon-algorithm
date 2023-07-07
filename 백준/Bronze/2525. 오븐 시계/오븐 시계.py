import sys

H, M = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

AH = H + ((M + T) // 60) # 조리되어 나오는 시
AM = (M + T) % 60 # 조리되어 나오는 분

if AH > 23: # 하루를 넘길때
    print(AH % 24, AM)
else: # 하루를 넘기지 않을때
    print(AH, AM)