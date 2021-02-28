alpha = input()
time = 0
for i in range(len(alpha)):
    a = alpha[i]
    if a in 'ABC':
        time += 3
    elif a in 'DEF':
        time += 4
    elif a in 'GHI':
        time += 5
    elif a in 'JKL':
        time += 6
    elif a in 'MNO':
        time += 7
    elif a in 'PQRS':
        time += 8
    elif a in 'TUV':
        time += 9
    else:
        time += 10

print(time)