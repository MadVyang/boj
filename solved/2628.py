from cmath import pi


w, h = [int(x) for x in input().split()]
paper = [[0]*w for _ in range(h)]
wcut = [[False]*(w+1) for _ in range(h+1)]
hcut = [[False]*(w+1) for _ in range(h+1)]
n = int(input())
for _ in range(n):
    c, i = [int(x) for x in input().split()]
    if c == 0:
        for j in range(w):
            wcut[i][j] = True
        continue
    else:
        for j in range(h):
            hcut[j][i] = True
        continue


def fill(i, j, c):
    if i < 0 or j < 0 or i >= h or j >= w or paper[i][j] != 0:
        return
    paper[i][j] = c
    if not hcut[i][j+1]:
        fill(i, j+1, c)
    if not wcut[i+1][j]:
        fill(i+1, j, c)


def print_paper():
    for i in range(h):
        print(' '.join([str(x) for x in paper[i]]))
    print()


piece = 1
for i in range(h):
    for j in range(w):
        if paper[i][j] == 0:
            fill(i, j, piece)
            piece += 1

count = [0]*piece
for i in range(h):
    for j in range(w):
        count[paper[i][j]] += 1
print(max(count[1:]))
