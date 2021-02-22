def selfnum(n):
    S = n
    n = '{}'.format(n)
    for i in range(len(n)):
        S = S + int(n[i])
    return S


d = list()
exa = set(range(1, 10001))

for i in range(1, 10001):
    # print(selfnum(i))
    d.append(selfnum(i))

dset = set(d)
sn = exa - dset
for i in range(len(sn)):
    print(sorted(list(sn))[i])

