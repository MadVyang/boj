from queue import Queue

A,B,C = map(int,input().split())

mem=[]
for i in range(A+1):
    mem.append([])
    for j in range(B+1):
        mem[i].append([])
        for k in range(C+1):
            mem[i][j].append(False)
        
case_queue = Queue()
case_queue.put((0,0,C))

while case_queue.qsize()>0:
    case = case_queue.get()
    if mem[case[0]][case[1]][case[2]]:
        continue
    mem[case[0]][case[1]][case[2]] = True

    # A
    if case[0]>0:
        # AB
        if case[0]+case[1]<B:
            case_queue.put((0,case[0]+case[1],case[2]))
        else:
            case_queue.put((case[0]+case[1]-B,B,case[2]))
        # AC
        if case[0]+case[2]<C:
            case_queue.put((0,case[1],case[0]+case[2]))
        else:
            case_queue.put((case[0]+case[2]-C,case[1],C))

    
    # B
    if case[1]>0:
        # BA
        if case[0]+case[1]<A:
            case_queue.put((case[0]+case[1],0,case[2]))
        else:
            case_queue.put((A,case[0]+case[1]-A,case[2]))
        # BC
        if case[1]+case[2]<C:
            case_queue.put((case[0],0,case[1]+case[2]))
        else:
            case_queue.put((case[0],case[1]+case[2]-C,C))
    

    # C
    if case[2]>0:
        # CA
        if case[0]+case[2]<A:
            case_queue.put((case[0]+case[2],case[1],0))
        else:
            case_queue.put((A,case[1],case[2]+case[0]-A))
        # CB
        if case[1]+case[2]<B:
            case_queue.put((case[0],case[1]+case[2],0))
        else:
            case_queue.put((case[0],B,case[1]+case[2]-B))

ans = list(map(lambda x: False, range(C+1)))

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i ==0 and mem[i][j][k]:
                ans[k]=True

s = ""
for i in range(0, C+1):
    if ans[i]:
        s += str(i)+" "
print(s)