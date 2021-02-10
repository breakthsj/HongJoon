import sys

#x = sys.stdin.read(1)
x = int(input())
# for i in range(int(x), 0, -1):
#     print(i)
print("\n".join(str(i) for i in range(int(x), 0, -1)))