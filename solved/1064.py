import math

ax, ay, bx, by, cx, cy = [int(x) for x in input().split()]

mn = int(9999999999999)
mx = int(0)


def update(d):
    global mn, mx

    if d < mn:
        mn = d
    if d > mx:
        mx = d


def dist(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    return math.sqrt(dx*dx+dy*dy)


if (bx-ax)*cy == (by-ay)*(cx-ax)+ay*(bx-ax):
    print(-1)
else:
    dx = cx+(bx-ax)
    dy = cy+(by-ay)
    update(2*(dist(ax, ay, bx, by)+dist(ax, ay, cx, cy)))

    dx = cx+(ax-bx)
    dy = cy+(ay-by)
    update(2*(dist(ax, ay, bx, by)+dist(bx, by, cx, cy)))

    dx = bx+(ax-cx)
    dy = by+(ay-cy)
    update(2*(dist(ax, ay, cx, cy)+dist(bx, by, cx, cy)))

    print(mx-mn)
