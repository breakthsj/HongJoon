import sys

L = list(map(int, sys.stdin.readlines()))
A = []
for i in L:
    A = A + [i%42]

S = set(A)
print(len(S))
