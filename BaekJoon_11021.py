import sys

T = int(input())
for i in range(1, T+1):
    x = sum(map(int, sys.stdin.readline(1).split()))
    print("Case #{}: {}".format(i, x))

# print("Case #{}: {}".format(i, x))