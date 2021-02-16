import sys

# while True:
#     S = sum(map(int, sys.stdin.readline().split()))
#     print(S)

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)