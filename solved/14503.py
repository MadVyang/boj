n, m = [int(x) for x in input().split()]
y, x, d = [int(x) for x in input().split()]
pan = []
for _ in range(n):
    pan.append([int(x) for x in input().split()])

clean = 0
bcount = 0
while True:
    if pan[y][x] == 0:
        pan[y][x] = 2
        clean += 1
    if d == 0:  # n
        if bcount == 4:
            if pan[y+1][x] == 1:
                break
            y += 1
            bcount = 0
            continue
        if pan[y][x-1] == 0:
            bcount = 0
            x -= 1
        else:
            bcount += 1
        d = 3
    elif d == 1:  # e
        if bcount == 4:
            if pan[y][x-1] == 1:
                break
            x -= 1
            bcount = 0
            continue
        if pan[y-1][x] == 0:
            bcount = 0
            y -= 1
        else:
            bcount += 1
        d = 0
    elif d == 2:  # s
        if bcount == 4:
            if pan[y-1][x] == 1:
                break
            y -= 1
            bcount = 0
            continue
        if pan[y][x+1] == 0:
            bcount = 0
            x += 1
        else:
            bcount += 1
        d = 1
    else:  # w
        if bcount == 4:
            if pan[y][x+1] == 1:
                break
            x += 1
            bcount = 0
            continue
        if pan[y+1][x] == 0:
            bcount = 0
            y += 1
        else:
            bcount += 1
        d = 2


print(clean)

# for i in range(n):
#     print(''.join([str(j) for j in pan[i]]))
