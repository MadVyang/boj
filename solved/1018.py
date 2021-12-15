N, M = map(int,input().split())
pan = []
for i in range(N):
    pan.append(input())

def check(y,x):
    count1 = 0
    count2 = 0
    for i in range(y,y+8):
        for j in range(x,x+8):
            if (i+j)%2==0 and pan[i][j]=="W":
                count1 += 1
            if (i+j)%2==1 and pan[i][j]=="B":
                count1 += 1
    for i in range(y,y+8):
        for j in range(x,x+8):
            if (i+j)%2==1 and pan[i][j]=="W":
                count2 += 1
            if (i+j)%2==0 and pan[i][j]=="B":
                count2 += 1
    return min((count1,count2))
                
ans = 50*50
for i in range(N-7):
    for j in range(M-7):
        r = check(i,j)
        if r < ans:
            ans = r

print(ans)
