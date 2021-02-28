import sys

N = input()
cnt = 0
for i in range(int(N)):
    word = sys.stdin.readline()
    ele = list(set(word))
    for e in ele:
        