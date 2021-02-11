import sys

T = int(input())

for x in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(x+1, a, b, a+b))