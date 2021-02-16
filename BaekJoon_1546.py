import sys

N = int(input())
S = list(map(int, sys.stdin.readline().split()))
Score = []
for i in range(N):
    Score.append(S[i]/max(S))
print(sum(Score)/N*100)