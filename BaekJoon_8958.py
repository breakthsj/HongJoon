import sys

N = int(input())


def fac(n):
    if n <= 1:
        return n
    else:
        sf = n + fac(n-1)
        return sf


for i in range(N):
    cnt = 0
    s = 0
    TC = sys.stdin.readline()
    for j in range(len(TC)-1):
        if TC[j] == 'O':
            cnt += 1
        else:
            s = s + fac(cnt)
            cnt = 0
    s = s + fac(cnt)
    print(s)
