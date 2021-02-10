import sys

T = int(input())
for i in range(T):
    print(sum(map(int, sys.stdin.readline().split())))