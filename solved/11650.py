N = int(input())

xys = []
for i in range(N):
    x,y = map(int,input().split())
    xys.append((x,y))
xys.sort(key=lambda xy: (xy[0],xy[1]))

for i in range(N):
    print(xys[i][0],xys[i][1])