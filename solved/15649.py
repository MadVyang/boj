N,M = map(int,input().split())

def dfs(selected,mask):
    if len(selected)==M:
        print_selected(selected)
        return
    for i in range(1,N+1):
        if (mask & (1<<i)) == 0:
            next_selected = selected.copy()
            next_selected.append(i)
            dfs(next_selected,mask | (1<<i))



def print_selected(selected):
    p = ""
    for s in selected:
        p+=str(s)+" "
    print(p)

dfs([],0)