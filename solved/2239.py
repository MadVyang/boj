arr = []
for i in range(9):
    arr.append([int(x) for x in input()])

ym = [set() for _ in range(9)]
xm = [set() for _ in range(9)]
gm = [
    [set() for _ in range(3)],
    [set() for _ in range(3)],
    [set() for _ in range(3)]
]

z = []

for i in range(9):
    for j in range(9):
        ym[i].add(arr[i][j])
        xm[j].add(arr[i][j])
        gm[i//3][j//3].add(arr[i][j])

        if arr[i][j] == 0:
            z.append((i, j))


def p():
    for i in arr:
        print(''.join([str(x) for x in i]))


solved = False


def solve(index):
    global solved
    if solved:
        return
    if index == len(z):
        if not solved:
            p()
            solved = True
        return

    y, x = z[index]

    for n in range(1, 10):
        if n in ym[y]:
            continue
        if n in xm[x]:
            continue
        if n in gm[y//3][x//3]:
            continue
        ym[y].add(n)
        xm[x].add(n)
        gm[y//3][x//3].add(n)
        arr[y][x] = n
        solve(index+1)
        ym[y].remove(n)
        xm[x].remove(n)
        gm[y//3][x//3].remove(n)
        arr[y][x] = 0


solve(0)
