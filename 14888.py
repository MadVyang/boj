N = int(input())
nums = list(map(int,input().split()))
num_op = list(map(int,input().split()))
ops = []
min=+1000000001
max=-1000000001


def dfs():
    global min,max
    if len(ops)==N-1:
        # print(ops)
        r=cal()
        # print(r)
        if min>r:
            min = r
        if max<r:
            max = r
        return
    for i in range(4):
        if check(i):
            index = len(ops)
            ops.append(i)
            dfs()
            ops.pop(index)


def check(t):
    count=0
    for op in ops:
        if op==t:
            count+=1
    if count==num_op[t]:
        return False
    return True


def cal():
    r = nums[0]
    for i in range(N-1):
        if ops[i]==0:
            r+=nums[i+1]
        elif ops[i]==1:
            r-=nums[i+1]
        elif ops[i]==2:
            r*=nums[i+1]
        else:
            if r<0 and nums[i+1]>0:
                r=-r
                r//=nums[i+1]
                r=-r
            else:
                r//=nums[i+1]
        # print(r)
    return r


dfs()
print(max)
print(min)