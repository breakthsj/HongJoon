import sys

L = list(map(int, sys.stdin.readlines()))

for i, v in enumerate(L):
    if v == max(L):
        print('{}\n{}'.format(v, (i+1)))
        