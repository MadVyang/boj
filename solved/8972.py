r, c = map(int, input().split())
bd = []

y, x = 0, 0
en = {}

for i in range(r):
    s = input()
    for j in range(c):
        if s[j] == 'R':
            en[(i, j)] = 1
        if s[j] == 'I':
            y, x = i, j

dir = [
    (0, 0),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

count = 0
for qr in input():
    qr = int(qr)
    y += dir[qr][0]
    x += dir[qr][1]
    count += 1
    if (y, x) in en:
        print('kraj', count)
        exit()

    nen = {}
    for ey, ex in en:
        if ey < y:
            ey += 1
        if ey > y:
            ey -= 1
        if ex < x:
            ex += 1
        if ex > x:
            ex -= 1
        if (ey, ex) == (y, x):
            print('kraj', count)
            exit()
        if (ey, ex) not in nen:
            nen[(ey, ex)] = 0
        nen[(ey, ex)] += 1
    en = {}
    for e in nen:
        if nen[e] == 1:
            en[e] = 1


for i in range(r):
    s = ''
    for j in range(c):
        if (i, j) in en:
            s += 'R'
        elif (i, j) == (y, x):
            s += 'I'
        else:
            s += '.'
    print(s)
