N = int(input())
l = []

for i in range(0,N):
    x,y = map(int,input().split())
    l.append((x,y))

ans = ""
for i in range(0,N):
    count = 0
    for j in range(0,N):
        if i==j:
            continue
        if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
            count += 1
    ans += str(count+1) +" "
print(ans)