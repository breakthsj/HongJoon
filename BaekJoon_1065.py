def hansu(n):
    if n < 100:
        return n
    else:
        cnt = 99
        for i in range(100, n+1):
            N = '{}'.format(i)
            d = int(N[0]) - int(N[1])
            if int(N[-1]) == int(N[0]) - d*(len(N)-1):
                print(N)
                cnt += 1
        return cnt


print(hansu(int(input())))