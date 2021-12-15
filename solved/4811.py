mem = []

for i in range(0,32):
    mem.append([])
    for j in range(0,32):
        mem[i].append(-1)

def sol(w,h):
    if w==0:
        return 1
    if h<0:
        return 0
    if mem[w][h]!=-1:
        return mem[w][h]
    r1=sol(w-1,h+1)
    r2=sol(w,h-1)
    mem[w][h]=r1+r2
    return r1+r2

while(True):
    n = int(input())
    if n==0:
        break
    print(sol(n,0))