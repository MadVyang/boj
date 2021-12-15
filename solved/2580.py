pan = []
for i in range(9):
    pan.append(list(map(int,input().split())))
zero_count=0
zeros=[]
y_nears = []
x_nears = []
box_nears = []
for i in range(9):
    yd = dict()
    xd = dict()
    for j in range(1,10):
        yd[j]=0
        xd[j]=0
    y_nears.append(yd)
    x_nears.append(xd)
for i in range(3):
    box_nears.append([])
    for j in range(3):
        bd = dict()
        for j in range(1,10):
            bd[j]=0
        box_nears[i].append(bd)

for i in range(9):
    for j in range(9):
        if pan[i][j]==0:
            zero_count+=1
            zeros.append((i,j))
        else:
            y_nears[i][pan[i][j]]+=1
            x_nears[j][pan[i][j]]+=1
            box_nears[i//3][j//3][pan[i][j]]+=1

def dfs(start,count):
    global is_clear
    if is_clear:
        return
    if count==zero_count:
        is_clear=True
        print_pan()
        return
    (y,x),next_start = get_target(start)
    # print()
    # print(y,x)
    for i in range(1,10):
        if is_possible(y,x,i):
            pan[y][x]=i
            y_nears[y][i]+=1
            x_nears[x][i]+=1
            box_nears[y//3][x//3][i]+=1
            # print_pan()
            dfs(next_start,count+1)
            pan[y][x]=0
            y_nears[y][i]-=1
            x_nears[x][i]-=1
            box_nears[y//3][x//3][i]-=1


def get_target(start):
    for i in range(start,len(zeros)):
        if pan[zeros[i][0]][zeros[i][1]]==0:
            return (zeros[i],(i+1)%len(zeros))
    for i in range(start,len(zeros)):
        if pan[zeros[i][0]][zeros[i][1]]==0:
            return (zeros[i],(i+1)%len(zeros))
    return (-1,-1,-1)


def is_possible(y,x,n):
    # nears = get_nears(y,x)
    # if n in nears:
    #     return False
    # return True
    if y_nears[y][n]>0:
        return False
    if x_nears[x][n]>0:
        return False
    if box_nears[y//3][x//3][n]>0:
        return False
    return True

    
def get_nears(y,x):
    r = dict()
    for i in range(0,9):
        if pan[y][i]!=0:
            r[pan[y][i]]=True
        if pan[i][x]!=0:
            r[pan[i][x]]=True
    Y=(y//3)*3
    X=(x//3)*3
    for i in range(3):
        for j in range(3):
            # print(y,x," ",i+Y,j+X)
            if pan[i+Y][j+X]!=0:
                r[pan[i+Y][j+X]]=True
    return r


def print_pan():
    for i in range(9):
        s=""
        for j in range(9):
            s+=str(pan[i][j])+" "
        print(s)


is_clear = False
dfs(0,0)