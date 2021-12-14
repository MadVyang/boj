N,M = map(int,input().split())

def dfs(selected):
    if len(selected)==M:
        print_selected(selected)
        return
    for i in range(1,N+1):
        next_selected = selected.copy()
        next_selected.append(i)
        dfs(next_selected)



def print_selected(selected):
    p = ""
    for s in selected:
        p+=str(s)+" "
    print(p)

dfs([])