import sys

N, X = map(int, sys.stdin.readline().split())
A =[]

for a in map(int, sys.stdin.readline().split()):
    if a < X:
        # A.append(a)
        print(a, end=" ")