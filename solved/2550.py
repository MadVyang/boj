n = int(input())
sws = {}
sw = [int(x) for x in input().split()]
lb = {}
idx = [int(x) for x in input().split()]
for i in range(n):
    lb[idx[i]] = i
# for i in range(n):
#     print(i, sw[i], lb[sw[i]])

trace = [0]*(n+1)
lis = []
for i in range(n):
    l = len(lis)
    if l == 0 or lis[l-1] < lb[sw[i]]:
        trace[lb[sw[i]]] = l
        lis.append(lb[sw[i]])
    else:
        left = 0
        right = l-1
        while left < right:
            mid = (left+right)//2
            if lb[sw[i]] <= lis[mid]:
                right = mid
            else:
                left = mid+1
        lis[right] = lb[sw[i]]
        trace[lb[sw[i]]] = right

cur = len(lis)-1
for i in range(n-1, -1, -1):
    if trace[lb[sw[i]]] == cur:
        lis[cur] = lb[sw[i]]
        cur -= 1

ans = []
for i in lis:
    ans.append(str(idx[i]))
ans.sort()
print(len(ans))
print(' '.join(ans))
