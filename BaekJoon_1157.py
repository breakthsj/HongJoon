import sys

word = sys.stdin.readline().lower()
fre = list()

for i in range(97, 123):
    fre.append(word.count(chr(i)))
if sorted(fre)[-2] == sorted(fre)[-1]:
    print('?')
else:
    print(chr(fre.index(max(fre))+97).upper())