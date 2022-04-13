s = input()
num = []
op = ['']

cur = 0
for c in s:
    if c == '+' or c == '-':
        num.append(cur)
        cur = 0
        op.append(c)
    else:
        cur *= 10
        cur += ord(c)-ord('0')
num.append(cur)
# print(num, op)

cur = num[0]
is_minus = False
for i in range(1, len(op)):
    if op[i] == '-':
        is_minus = True
    if is_minus:
        cur -= num[i]
    else:
        cur += num[i]
    # print(cur)
print(cur)
