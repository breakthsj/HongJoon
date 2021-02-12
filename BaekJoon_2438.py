N = int(input())

for i in range(1, N+1):
    print("{}".format("*"*i), end="")
    if i != N:
        print()