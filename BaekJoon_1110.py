N = input()
A = N
cnt = 0

while True:
    if (int(N) == int(A)) & (cnt != 0):
        break
    if len(N) == 1:
        N = "0"+N
    N = N[1] + "{}".format((int(N[0]) + int(N[1])) % 10)
    cnt += 1

print(cnt)