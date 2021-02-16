import sys

C = int(input())

for case in range(C):
    N, *score = map(int, sys.stdin.readline().split())
    mean = sum(score)/N
    cnt = 0
    for student in score:
        if student > mean:
            cnt += 1
    print('{:.3f}%'.format(round(cnt/N*100, 3)))