N = int(input())

ans = 0
def dfs(count,check):
    global ans
    if count==N:
        ans+=1
        return
    for i in range(N):
        if check[count*N+i] == False:
            next_check=check.copy()
            indexs=[]
            for j in range(N):
                indexs.append(count*N+j)
                indexs.append(j*N+i)
                if count>=j and i>=j:
                    indexs.append((count-j)*N+i-j)
                if count+j<N and i+j<N:
                    indexs.append((count+j)*N+i+j)
                if count>=j and i+j<N:
                    indexs.append((count-j)*N+i+j)
                if count+j<N and i>=j:
                    indexs.append((count+j)*N+i-j)
            for index in indexs:
                next_check[index]=True
            dfs(count+1,next_check)
dfs(0,[False]*N*N)
print(ans)