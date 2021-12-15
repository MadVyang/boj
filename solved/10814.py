N = int(input())

mems = []
for i in range(N):
    line = input().split()
    mems.append((int(line[0]),line[1]))
mems.sort(key=lambda xy: (xy[0]))

for i in range(N):
    print(mems[i][0],mems[i][1])