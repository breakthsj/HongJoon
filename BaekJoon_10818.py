import sys

N = input()
L = list(map(int, sys.stdin.readline().split()))
print("{} {}".format(min(L), max(L)))