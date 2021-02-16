import sys


while True:
    S = sum(map(int, sys.stdin.readline().split()))
    if S ==0:
        break
    print(S)