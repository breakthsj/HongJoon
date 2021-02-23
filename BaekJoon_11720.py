import sys

N = int(input())
n = sys.stdin.readline()
S = 0
for i in range(N):
    S = S + int(n[i])
print(S)