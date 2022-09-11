string = input()
sum=0
letter = []
for i in string:
    if ord('0') <= ord(i) <= ord('9'):
        sum+=int(i)
    else:
        letter.append(i)

letter.sort()
if sum != 0:
    letter.append(str(sum))

# for l in letter:
#     print(l, end='')

print(''.join(letter))