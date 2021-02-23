import sys

nums = list(map(''.join, map(list, map(reversed, sys.stdin.readline().split()))))
print(max(list(map(int, nums))))