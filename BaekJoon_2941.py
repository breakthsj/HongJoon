word = input()
croalpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt2 = 0
cnt3 = 0
for i in range(len(word)-1):
    if (word[i]+word[i+1]) in croalpha:
        cnt2 += 1
    if i < len(word)-2:
        if (word[i]+word[i+1]+word[i+2]) == 'dz=':
            cnt3 += 1
            cnt2 -= 1
print(len(word)-cnt2 - 2*cnt3)