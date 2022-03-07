n = input()
sum = 0
ten = False
three = False
for c in n:
    sum += int(c)
    if c == '0':
        ten = True
if sum % 3 == 0:
    three = True
# print(ten, three)
if ten and three:
    tmp = [c for c in n]
    tmp.sort(reverse=True)
    print(''.join(tmp))
else:
    print(-1)
