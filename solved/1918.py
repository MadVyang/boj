from collections import deque


s = input()

oq = deque()
aq = deque()


for c in s:
    if c == '(':
        oq.append(c)
    elif c == ')':
        while oq and oq[-1] != '(':
            aq.append(oq.pop())
        oq.pop()
    elif c in ['*', '/', '+', '-']:
        if c in ['*', '/']:
            while oq and oq[-1] in ['*', '/']:
                aq.append(oq.pop())
        else:
            while oq and oq[-1] != '(':
                aq.append(oq.pop())
        oq.append(c)
    else:
        aq.append(c)

while oq:
    aq.append(oq.pop())

print(''.join(aq))
