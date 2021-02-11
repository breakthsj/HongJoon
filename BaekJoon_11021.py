import sys

T = int(input())

for i in range(T):
    print("Case #{}: {}".format(int(i)+1, sum(map(int, sys.stdin.readline().split()))))
