import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

for i in range(10):
    cnt = 0
    for j in '{}'.format(A*B*C):
        if i == int(j):
            cnt += 1
    print(cnt)
